from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
producer.send('sample', b'Om Sai Ram')
producer.send('sample',key=b'message-2', value=b'Shri Sai Ram')
producer.flush(30)