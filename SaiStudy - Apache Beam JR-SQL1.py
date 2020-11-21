import typing


from apache_beam.portability.common_urns import coders
from apache_beam.transforms.sql import SqlTransform
from past.builtins import unicode

Purchase = typing.NamedTuple('Purchase',
                             [('item_name', unicode), ('price', float)])
coders.registry.register_coder(Purchase, coders.RowCoder)

xx = Purchase | SqlTransform("""
              SELECT item_name, COUNT(*) AS `count`
              FROM PCOLLECTION GROUP BY item_name""")
