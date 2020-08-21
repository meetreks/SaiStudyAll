from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
import mlflow
import mlflow.spark
import pandas as pd

if __name__ == "__main__":
    # Create a SparkSession
    spark = (SparkSession
             .builder
             .appName("Example-3_6")
             .getOrCreate())
sf_fire_file = "sairam.parquet"
airbnbDF = spark.read.parquet(sf_fire_file)
trainDF, testDF = airbnbDF.randomSplit([.8, .2], seed=42)
categoricalCols = [field for (field, dataType) in trainDF.dtypes if dataType == "string"]
indexOutputCols = [x + "Index" for x in categoricalCols]
stringIndexer = StringIndexer(inputCol=str(categoricalCols),
                              outputCol=str(indexOutputCols),
                              handleInvalid="skip")
numericCols = [field for (field, dataType) in trainDF.dtypes
               if ((dataType == "double") & (field != "price"))]
assemblerInputs = indexOutputCols + numericCols
vecAssembler = VectorAssembler(inputCols=assemblerInputs,
                               outputCol="features")
rf = RandomForestRegressor(labelCol="price", maxBins=40, maxDepth=5,
                           numTrees=100, seed=42)
pipeline = Pipeline(stages=[stringIndexer, vecAssembler, rf])

with mlflow.start_run(run_name="random-forest") as run:
# Log params: num_trees and max_depth
    mlflow.log_param("num_trees", rf.getNumTrees())
    mlflow.log_param("max_depth", rf.getMaxDepth())
# Log model
    pipelineModel = pipeline.fit(trainDF)
    mlflow.spark.log_model(pipelineModel, "model")
# Log metrics: RMSE and R2
    predDF = pipelineModel.transform(testDF)
    regressionEvaluator = RegressionEvaluator(predictionCol="prediction",
                                          labelCol="price")
    rmse = regressionEvaluator.setMetricName("rmse").evaluate(predDF)
    r2 = regressionEvaluator.setMetricName("r2").evaluate(predDF)
    mlflow.log_metrics({"rmse": rmse, "r2": r2})
# Log artifact: feature importance scores
    rfModel = pipelineModel.stages[-1]
    pandasDF = (pd.DataFrame(list(zip(vecAssembler.getInputCols(),
                                  rfModel.featureImportances)),
                         columns=["feature", "importance"])
            .sort_values(by="importance", ascending=False))
# First write to local filesystem, then tell MLflow where to find that file
    pandasDF.to_csv("feature-importance.csv", index=False)
    mlflow.log_artifact("feature-importance.csv")