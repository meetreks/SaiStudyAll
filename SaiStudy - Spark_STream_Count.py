import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
if __name__ == "__main__":
# Create a SparkSession
    sc = SparkContext(appName="Sai-Streaming")
    ssc = StreamingContext(sc,2)
    ssc.checkpoint("checkpoint")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    #lines = ssc.socketTextStream("localhost", 9999)
    lines.pprint()

    def countWords(newVaues, lastSum):
        if lastSum is None:
            lastSum = 0
        return sum(newVaues, lastSum)

    word_counts = lines.flatMap(lambda line: line.split(" "))\
        .map(lambda word: (word,1))\
        .updateStateByKey(countWords)

    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()

#for starting this go to Terminal
#spark-submit "C:\SaiStudy - LEarn It All - Version9\SaiStudy - Spark_STream_Count.py" 192.168.56.1 9999
#nc -Lp 9999
#Excellent this is workign like a treat maddy - good job