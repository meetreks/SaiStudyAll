import json
import socket
from TwitterAPI import TwitterAPI

if __name__ == "__main__":
    consumer_api_key = "heaViJzA1YzxP8p1fMVnkG7C7"
    consumer_api_secret = "OD9OaDIm7K5ab4zMSisSE1eW3o7cjulhfj5CwV3jmxjJfEPRus"

    access_api_key = "230085799-4kYtfW4OKceG6YdXEqEnrvqKAdjGXIdv4iRxoWTq"
    access_api_secret = "3zBMj7bcX1giVqvWMNuVVE8ghF5j8AlndaLjftUWwLR5o"
    api = TwitterAPI(consumer_api_key,consumer_api_secret,access_api_key,access_api_secret)
    TRACK_TERM = '#'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.56.1', 7777)
    sock.connect(server_address)

    host = '192.168.56.1'
    port = 7777
    addr = (host,port)
    sock.bind((host,port))
    sock.listen(5)


    r = api.request('statuses/filter', {'track': TRACK_TERM})
    for item in r:
        result = json.dumps(item)
        m1 = json.loads(result)
        m2 = m1['text'].encode('utf-8')
        sock.send(m2)
# to make this work
#nc -Lp 23456
#then run this program and you can see twitter streaming to a server listening at 23456