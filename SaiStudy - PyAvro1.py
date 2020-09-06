import json
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
schema = {
    "type": "record",
    "namespace": "sailearning.schema",
    "name": "User",
    "fields": [{"name": "userid", "type": "string"},
               {"name": "username", "type": "string"}]
}
#file_str = open(file="schema.avsc")
#schema = file_str.read()
print(schema)
write_schema = avro.schema.Parse(json.dumps(schema))
writer = DataFileWriter(open("users1.avro", "wb"), DatumWriter(), write_schema)
writer.append({"userid": "Sairam9", "username": "OmSairam9"})
writer.append({"userid": "SaiRitvik9", "username": "LittleSinghamRitvik"})
writer.close()

reader = DataFileReader(open("users1.avro", "rb"), DatumReader())
for user in reader:
    print(user)

reader.close()