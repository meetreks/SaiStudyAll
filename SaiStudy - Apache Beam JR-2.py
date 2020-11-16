import apache_beam as beam
import re
def split_words(text):
    return text.split(',')

input = ["1200,Amex",
         "1200,Visa",
         "1200,Amex",
         "1200,Visa",
         "1200,Mcard"
         ]
with beam.Pipeline() as pipeline:
    plants = (
            pipeline
            | 'Create Input' >> beam.Create(input)
            | 'Split words' >> beam.FlatMap(split_words)
            | 'SUm the stuff' >> beam.combiners.Count.PerElement()
            #| 'Split words' >> beam.FlatMap(str.split)
            #| 'Flatten lists' >> beam.FlatMap(lambda elements: elements)
            | beam.Map(print))