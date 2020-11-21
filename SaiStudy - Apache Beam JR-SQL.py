import apache_beam as beam
from apache_beam.transforms.sql import SqlTransform
import typing


class Transaction(typing.NamedTuple):
    bank: str
    purchase_amount: float


# Running locally in the DirectRunner.
input_pc = [{
    "bank": 'Om Sai Ram',
    "purchase_amount": 9999.99

},
    {
        "bank": 'Om Sai Ram1',
        "purchase_amount": 99999.99
    }
]
output_pc = input_pc | beam.Map(lambda item: beam.Row(bank=str(item["bank"]),
                                                      purchase_amount=float(item["purchase_amount"])))
print(output_pc)
sql_pc = output_pc | SqlTransform("SELECT * FROM PCOLLECTION")


