from kafka import KafkaProducer
#Greg - before starting - pip install slackclient

from slack import AsyncWebClient as wc

#Greg -- please change to the Ip of your KAFKA cluster and port please
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
#Greg -- Please use your Oauth token
tk = "PLEASE HARD CODE YOUR TOKEN HERE"
chan = wc(tk)
message_list = chan.api_call("channels.history", channel="random", oldest=0, count="1000")
for m in message_list["messages"]:
    producer.send('random', m)
    producer.flush(30)