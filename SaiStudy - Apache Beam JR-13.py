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
        elt = {}
        make = x[0]
        price = float(x[1])/100
        #elt[make] = price
        #yield elt
        yield make,price

def partition_fn(element, num_partitions):
    make,values = element
    print(values)
    if(int(values) < 2000):
        print(values)
        return 0
    elif(int(values) < 5000):
        print(values)
        return 1
    elif(int(values) < 10000):
        print(values)
        return 2
    else:
        print(values)
        return 3


# The Problem with this module is I need a PCollection of KV pairs and not KV pairs.
with beam.Pipeline() as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par Do' >> beam.ParDo(Head())
            | 'Par D1' >> beam.ParDo(Split())
            | 'Par D2' >> beam.Partition(partition_fn,4)
            | 'Par D3' >> beam.Map(print)

    )
#prtn = pipeline | 'Par D2' >> beam.Partition(partition_fn,4)
#p2 = prtn[2]
#print(p2)
