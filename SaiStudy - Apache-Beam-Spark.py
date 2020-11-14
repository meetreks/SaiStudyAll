import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import re
import os

from apache_beam.runners.portability.portable_runner import PortableRunner
from apache_beam.runners.portability.spark_runner import SparkRunner

inputs_pattern = 'inpt.txt'
outputs_prefix = 'outputs/part1'
options = PipelineOptions([
    "--runner=PortableRunner",
    "--job_endpoint=localhost:8099",
    "--environment_type=LOOPBACK"
])
#options = PipelineOptions()
#options = PipelineOptions([
#    "--runner=FlinkRunner",
#    "--flink_version=1.8",
#    "--flink_master=localhost:8081",
#    "--environment_type=LOOPBACK"
#])
#if os.environ.get('http_proxy'):
#    del os.environ['http_proxy']
print(options.get_all_options())
with beam.Pipeline(options=options) as pipeline:
    (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(inputs_pattern)
            | 'Find words' >> beam.FlatMap(lambda line: re.findall(r"[a-zA-Z']+", line))
            | 'Pair words with 1' >> beam.Map(lambda word: (word, 1))
            | 'Group and sum' >> beam.CombinePerKey(sum)
            | 'Format results' >> beam.Map(lambda word_count: str(word_count))
            | 'Write results' >> beam.io.WriteToText(outputs_prefix)
    )