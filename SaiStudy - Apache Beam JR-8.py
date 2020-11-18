import apache_beam as beam
from datetime import datetime
file_in = 'car_ad.csv'
skip_head = "car,price,body,mileage,engV,engType,registration,year,model,drive"

class Head(beam.DoFn):
    def process(self, element):

        if (element!= skip_head):
            yield element



class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        elt = {}
        make = x[0]
        cy = datetime.now().year
        age = cy - int(x[7])
        elt[make] = age
        yield elt

# Running locally in the DirectRunner.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D3' >> beam.Map(print)
    )