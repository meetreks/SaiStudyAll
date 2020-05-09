from kafka import KafkaConsumer
settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = KafkaConsumer(bootstrap_servers = 'localhost:9092')

c.subscribe(['sample'])

for message in c:
    print(message)

c.close()
