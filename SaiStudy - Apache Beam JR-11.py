import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

file_in = 'Mall_Customers.csv'
skip_head = "CustomerID,Genre,Age,Annual Income,Spending Score"

class Head(beam.DoFn):
    def process(self, element):

        if (element!= skip_head):
            yield element



class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        make = x[0]
        model = x[3]
        yield make,model

class Split1(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        make = x[0]
        model = x[4]
        yield make,model

# The Problem with this module is I need a PCollection of KV pairs and not KV pairs.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D2' >> beam.GroupByKey()
            | 'Par D4' >> beam.Map(print)
    )

with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D2' >> beam.GroupByKey()
            | 'Par D4' >> beam.Map(print)
    )