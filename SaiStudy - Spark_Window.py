import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
if __name__ == "__main__":
# Create a SparkSession
    sc = SparkContext(appName="Sai-Streaming")
    ssc = StreamingContext(sc,2)
    ssc.checkpoint("checkpoint")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    counts = lines.countByWindow(10,2)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()

#for starting this go to Terminal
#spark-submit "C:\SaiStudy - LEarn It All - Version9\SaiStudy - Spark_STream_Count.py" 192.168.56.1 9999
#nc -Lp 9999
#Excellent this is workign like a treat maddy - good job