from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


c = AvroConsumer({
    'bootstrap.servers': 'http://192.168.99.102:29092',
    'group.id': 'groupid',
    'schema.registry.url': 'http://192.168.99.102:8081'})

c.subscribe(['my_topic'])

while True:
    try:
        msg = c.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue

    print(msg.value())

c.close()