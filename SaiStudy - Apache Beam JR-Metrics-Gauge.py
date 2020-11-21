import apache_beam as beam
from apache_beam.metrics import Metrics
from apache_beam.metrics.metric import MetricsFilter

file_in = 'car_ad.csv'
skip_head = "car,price,body,mileage,engV,engType,registration,year,model,drive"

class Head(beam.DoFn):
    def __init__(self):
        self.empty_line_counter = Metrics.gauge('main','empty_lines')

    def process(self, element):

        if (element!= skip_head):
            x = element.split(",")
            y= float(x[1])/100
            self.empty_line_counter.set(y)
            yield element



class Split(beam.DoFn):
    def __init__(self):
        self.word_length_counter = Metrics.gauge('main','word_lengths')


    def process(self, element):
        x = element.split(",")
        y = x[2]
        z = float(x[1])/100
        if(y == "sedan") or (y == "hatch"):
            self.word_length_counter.set(z)
            yield element

class Filter(beam.DoFn):
    def __init__(self):
        self.word_counter = Metrics.gauge('main','total_words')

    def process(self, element):
        x = element.split(",")
        y= float(x[1])/100

        if y < 200.0:
            self.word_counter.set(y)
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
pr = pipeline.run()
pr.wait_until_finish()
empty_lines_filter = MetricsFilter().with_name('empty_lines')
query_result = pr.metrics().query(empty_lines_filter)
print(query_result)

word_lengths_filter = MetricsFilter().with_name('word_lengths')
query_result = pr.metrics().query(word_lengths_filter)
print(query_result)


tot_len_filter = MetricsFilter().with_name('total_words')
query_result = pr.metrics().query(tot_len_filter)
print(query_result)