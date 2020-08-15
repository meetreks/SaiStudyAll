from ksql import KSQLAPI
client = KSQLAPI('http://192.168.99.100:8088')
s = client.ksql('show streams')
print(s)