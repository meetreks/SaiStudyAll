import apache_beam as beam

inputs_pattern = 'SalesJan2009.csv'

class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        y = x[0],x[1],x[2],x[3],x[4]
        yield y

# Running locally in the DirectRunner.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(inputs_pattern)
            | 'Par Do' >> beam.ParDo(Split())
            | 'Try1' >> beam.Map(print)
    )