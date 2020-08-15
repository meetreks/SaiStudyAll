import sys
import sched, time

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.clustering import StreamingKMeans

if __name__ == "__main__":
    sc = SparkContext(appName="sai twitter feed")
    ssc = StreamingContext(sc,10)

    ssc.checkpoint("chkpfile")
    def parserData(line):
        cells = line.split(",")
        return Vectors.dense([float(cells[0]), float(cells[1])])
    trainingStream = ssc.textFileStream("/files").map(parserData)

    model = StreamingKMeans(k=2, decayFactor=1.0).setRandomCenters(2, 1.0, 0)
    print("Initial Centres" + str(model.latestModel().centers))
    model.trainOn(trainingStream)
    ssc.start()

    s = sched.scheduler(time.time, time.sleep)
    def print_cluster_centres(sc, model):
        print(str(model.latestModel().centers))
        s.enter(10, 1, print_cluster_centres, (s, model))

    s.enter(10, 1, print_cluster_centres, (s, model))
    s.run()

    ssc.awaitTermination()
# to make this work
#spark-submit "C:\SaiStudy - LEarn It All - Version9\Saistudy - split-csv.py"