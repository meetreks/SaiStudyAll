import pyspark

sc = pyspark.SparkContext(appName="sai_transformation")
print(sc._conf.getAll())
students = sc.textFile("students.csv")
print(students.collect())
ss = students.filter(lambda row: 'a' in row)
print(ss.collect())