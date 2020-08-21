from pyspark.sql import SparkSession

# Main program
from pyspark.sql.functions import split


if __name__ == "__main__":
# Create a SparkSession
    spark = (SparkSession
         .builder
         .appName("Example-3_6")
         .getOrCreate())
    lines = (spark
         .readStream.format("socket")
         .option("host", "192.168.56.1")
         .option("port", 9999)
         .load())

    words = lines.select(split('value', ' ').alias('word'))
    counts = words.groupBy("word").count()
    checkpointDir = "/checkpoint"
    streamingQuery = (counts
                  .writeStream
                  .format("console")
                      .outputMode("complete")
                      .trigger(processingTime="1 second")
                      .option("checkpointLocation", checkpointDir)
                      .start())

    streamingQuery.awaitTermination()

# To make this work
#nc -Lp 9999 and start typing stuff and just use the run button and it will work
#Excellent this is workign like a treat maddy - good job