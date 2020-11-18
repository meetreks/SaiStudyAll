import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

file_in = 'car_ad.csv'
skip_head = "car,price,body,mileage,engV,engType,registration,year,model,drive"

class Head(beam.DoFn):
    def process(self, element):

        if (element!= skip_head):
            yield element



class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        make = x[0]
        model = x[1]
        yield make,model

class Average(beam.DoFn):
    def process(self, element):
        make,values = element
        count = 0
        sumPrice = 0
        for price in values:
            sumPrice = sumPrice + float(price)
            count = count + 1
        yield make,sumPrice/count

# The Problem with this module is I need a PCollection of KV pairs and not KV pairs.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D2' >> beam.GroupByKey()
            | 'Par D3' >> beam.ParDo(Average())
            | 'Par D4' >> beam.Map(print)
    )