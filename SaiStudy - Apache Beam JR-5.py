import csv

import apache_beam as beam

inputs_pattern = 'SalesJan2009.csv'
outputs_prefix = 'outputs/part'

def print_row(element):
    print(element)

def parse_file(element):
    for line in csv.reader([element], delimiter=','):
        return line

# Running locally in the DirectRunner.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(inputs_pattern)
            | 'Par Do' >> beam.Map(parse_file)
            | 'Try1' >> beam.Map(print_row)
    )