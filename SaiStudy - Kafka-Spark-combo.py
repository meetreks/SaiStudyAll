import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import pykafka

class TweetsListen(StreamListener):
    def __init__(self, kafkaProducer):
        self.producer = kafkaProducer

    def on_data(self, raw_data):
        json_data = json.loads(raw_data)
        words = json_data["text"].split()
        htl = list(filter(lambda x: x.lower().startswith("#"), words))
        if(len(htl)!=0):
            for ht in htl:
                self.producer.produce(bytes(ht,"utf-8"))
        return True

def connect_to_twitter(kafkaProducer, tracks):
    consumer_api_key = "heaViJzA1YzxP8p1fMVnkG7C7"
    consumer_api_secret = "OD9OaDIm7K5ab4zMSisSE1eW3o7cjulhfj5CwV3jmxjJfEPRus"

    access_api_key = "230085799-4kYtfW4OKceG6YdXEqEnrvqKAdjGXIdv4iRxoWTq"
    access_api_secret = "3zBMj7bcX1giVqvWMNuVVE8ghF5j8AlndaLjftUWwLR5o"

    auth = OAuthHandler(consumer_api_key,consumer_api_secret)
    auth.set_access_token(access_api_key, access_api_secret)

    twitter_stream = Stream(auth,TweetsListen(kafkaProducer))
    twitter_stream.filter(track=tracks, languages=["en"])


if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[1]
    topic = sys.argv[1]
    tracks = sys.argv[1]

    kafkaClient = pykafka.KafkaClient("192.168.56.1:9092")
    kafkaProducer = kafkaClient.topics[bytes(topic,"utf-8")].get_producer()
    connect_to_twitter(kafkaProducer, tracks)

#to tun this on the terminal type
#python "SaiStudy - Kafka-Spark-combo.py" localhost 9092 sai_topic "sairam"