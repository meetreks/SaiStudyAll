from pyspark.sql.types import *
from pyspark.sql import Column
from pyspark.sql import SparkSession
fire_schema = StructType([StructField('CallNumber', IntegerType(), True),
                          StructField('UnitID', StringType(), True),
                          StructField('IncidentNumber', IntegerType(), True),
                          StructField('CallType', StringType(), True),
                          StructField('CallDate', StringType(), True),
                          StructField('WatchDate', StringType(), True),
                          StructField('CallFinalDisposition', StringType(), True),
                          StructField('AvailableDtTm', StringType(), True),
                          StructField('Address', StringType(), True),
                          StructField('City', StringType(), True),
                          StructField('Zipcode', IntegerType(), True),
                          StructField('Battalion', StringType(), True),
                          StructField('StationArea', StringType(), True),
                          StructField('Box', StringType(), True),
                          StructField('OriginalPriority', StringType(), True),
                          StructField('Priority', StringType(), True),
                          StructField('FinalPriority', IntegerType(), True),
                          StructField('ALSUnit', BooleanType(), True),
                          StructField('CallTypeGroup', StringType(), True),
                          StructField('NumAlarms', IntegerType(), True),
                          StructField('UnitType', StringType(), True),
                          StructField('UnitSequenceInCallDispatch', IntegerType(), True),
                          StructField('FirePreventionDistrict', StringType(), True),
                          StructField('SupervisorDistrict', StringType(), True),
                          StructField('Neighborhood', StringType(), True),
                          StructField('Location', StringType(), True),
                          StructField('RowID', StringType(), True),
                          StructField('Delay', FloatType(), True)])
if __name__ == "__main__":
# Create a SparkSession
    spark = (SparkSession
         .builder
         .appName("Example-3_6")
         .getOrCreate())
sf_fire_file = "Fire_Incidents.csv"
fire_df = spark.read.csv(sf_fire_file, header=True, schema=fire_schema)
print(fire_df.columns)
#this was very quick, life a million rows less than a second.
#parquet_path = "/parquet-file/"
#fire_df.write.format("parquet").save(parquet_path)

# the below code should fail, as I have no clusters running for table sai-parquet-table
#parquet_table = "sai-parquet-table"
#fire_df.write.format("parquet").saveAsTable(parquet_table)

few_fire_df = (fire_df
               .select("IncidentNumber", "AvailableDtTm", "CallType")
               .where(fire_df["CallType"] != "Medical Incident"))
few_fire_df.show(5, truncate=False)