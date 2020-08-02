import pyspark
from pyspark.streaming import StreamingContext
import sys

sc = pyspark.SparkContext(appName="sai_transformation")
ssc = StreamingContext(sc,2)
ssc.checkpoint("spark_ssc")

lines = sc.textFile("random.txt")
words = lines.flatMap(lambda li : li.split(" "))
print(words.collect())
counts = words.map(lambda word : (word, 1)).reduceByKey(lambda a, b: a+b)
print(counts.collect())

