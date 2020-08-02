import pyspark

sc = pyspark.SparkContext(appName="sai_transformation")
lines = sc.textFile("random.txt")
words = lines.flatMap(lambda li : li.split(" "))
print(words.collect())
counts = words.map(lambda word : (word, 1)).reduceByKey(lambda a, b: a+b)
print(counts.collect())

