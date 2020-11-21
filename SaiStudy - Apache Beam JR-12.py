import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.combiners import Mean


file_in = 'Mall_Customers.csv'
skip_head = "CustomerID,Genre,Age,Annual Income,Spending Score"

class Head(beam.DoFn):
    def process(self, element):

        if (element!= skip_head):
            yield element



class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        age = x[2]
        yield int(age)

def Split1(element):
    print(element)
    sum = 0
    count = 0
    for x in element:
        sum = sum + x
        count = count + 1
    return sum/count

# The Problem with this module is I need a PCollection of KV pairs and not KV pairs.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            #| 'Par D2' >> beam.CombineGlobally(Split1)
            | 'Par D2' >> beam.CombineGlobally(beam.combiners.MeanCombineFn())
            | 'Par D4' >> beam.Map(print)
    )

