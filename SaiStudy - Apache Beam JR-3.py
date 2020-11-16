import apache_beam as beam
import re

inputs_pattern = 'SalesJan2009.csv'
outputs_prefix = 'outputs/part'

class SplitWords(beam.DoFn):
    def __init__(self, header):
        self.header = header

    def process(self, text):
        yield text

# Running locally in the DirectRunner.
header = "Date,Product,Price,Card,Country"
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(inputs_pattern)
            | 'Par Do' >> beam.ParDo(SplitWords(header))
            | 'SUm the stuff' >> beam.combiners.Count.PerElement()
            #| 'Find words' >> beam.FlatMap(lambda line: re.split(",", line))
            | 'Format results' >> beam.Map(print)
            #| 'Write results' >> beam.io.WriteToText(outputs_prefix)
    )