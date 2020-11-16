import apache_beam as beam

class SplitWords(beam.DoFn):
    def __init__(self, delimiter=','):
        self.delimiter = delimiter

    def process(self, text):
        for word in text.split(self.delimiter):
            yield word
input = ["1200,Amex",
         "1200,Visa",
         "1200,Amex",
         "1200,Visa",
         "1200,Mcard"
         ]
with beam.Pipeline() as pipeline:
    plants = (
            pipeline
            | 'Gardening plants' >> beam.Create(input)
            | 'Split words' >> beam.ParDo(SplitWords(','))
            | beam.Map(print))