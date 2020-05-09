import json
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.Parse(json.dumps({
    "namespace"    : "example.avro",
    "type"         : "record",
    "name"         : "User",
    "fields"       : [
        {"name": "name"            , "type": "string"},
        {"name": "favorite_number" , "type": ["int", "null"]},
        {"name": "favorite_color"  , "type": ["string", "null"]}
    ]
}))
#print(schema)
writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)

reader.close()