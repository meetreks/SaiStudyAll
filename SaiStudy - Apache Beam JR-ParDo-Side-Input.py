import apache_beam as beam

file_in = 'tags.csv'
skip_head = "Date,Open,High,Low,Close,Adj Close,Volume"

class Head(beam.DoFn):
    def process(self, element):

        if (element!= skip_head):
            yield element



class Split(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        y = x[2]
        if(y == "sedan") or (y == "hatch"):
            yield element

class Filter(beam.DoFn):
    def process(self, element):
        x = element.split(",")
        y= float(x[1])/100

        if y < 200.0:

            yield element

class Print_Row(beam.DoFn):
    def process(self, element):
        print(element)
# Running locally in the DirectRunner.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D2' >> beam.ParDo(Filter())
            | 'Par D3' >> beam.Map(print)
    )