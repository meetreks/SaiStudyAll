from pyspark.sql import SparkSession

if __name__ == "__main__":
# Create a SparkSession
    spark = (SparkSession
         .builder
         .appName("SaiSparkSQLEngine")
         .getOrCreate())
sf_fire_file = "Fire_Incidents.csv"
fire_df = (spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(sf_fire_file))
fire_df.createOrReplaceTempView("fire_incidents")
(fire_df.select("Arrival_DtTm").where("Arrival_DtTm != null").show(10))
spark.sql("""SELECT * FROM fire_incidents WHERE Arrival_DtTm is NOT NULL""").show(10)
#so effectivley what we are saying is - use RDD, DF or SQL to achieve the same result.