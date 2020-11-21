import apache_beam as beam
import csv
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import window
from datetime import datetime

file_in = 'tags.csv'
skip_head = "userId,movieId,tag,timestamp"


class ParseNewMovies(beam.DoFn):
    def process(self,element):
        if(element!= skip_head):
            z = element.split(",")
            y=int(z[3])
            i = datetime.utcfromtimestamp(y)
            x = i.strftime('%Y-%m-%d %H:%M:%S')
            yield {
                'userId': z[0],
                'movieID': z[1],
                'tag': z[2],
                'timestamp': x
            }


with beam.Pipeline() as pipeline:
    item = (

            pipeline
            | 'Read lines' >> beam.io.ReadFromText(file_in)
            | 'Par D1' >> beam.ParDo(ParseNewMovies())


    )
    x = (
        item | 'Par D3' >>  beam.WindowInto(window.FixedWindows(5))
             | 'Par D4' >>  beam.Map(print)
    )

