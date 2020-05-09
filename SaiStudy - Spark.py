import pyspark
import os
#os.environ['SPARK_HOME'] = "C:/spark-binaries/spark-2.4.4-bin-hadoop2.7/bin"
sc = pyspark.SparkContext(appName="maps_and_lazy_evaluation_example")
print(sc._conf.getAll())

log_of_songs = [
    "Despacito",
    "Nice for what",
    "No tears left to cry",
    "Despacito",
    "Havana",
    "In my feelings",
    "Nice for what",
    "despacito",
    "All the stars"
]

# parallelize the log_of_songs to use with Spark
distributed_song_log = sc.parallelize(log_of_songs)
#distributed_song_log.map(lambda song: song.lower()).collect()
def convert_song_to_lowercase(song):
    return song.lower()

convert_song_to_lowercase("Havana")

distributed_song_log.map(convert_song_to_lowercase)
distributed_song_log.map(convert_song_to_lowercase).collect()
