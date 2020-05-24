from ksql import KSQLAPI
client = KSQLAPI('http://localhost:8088')
s = client.ksql('show streams')
print(s)