import json
from pathlib import Path
from pprint import pprint

import pandas as pd
from ixbrlparse import IXBRL
import xbrl

class 

# TODO: consts file
RESOURCES = Path('../tests/resources')
fin1 = RESOURCES / 'fin1-xbrl.html'
fin2 = RESOURCES / 'fin2-xbrl.html'
fin3 = RESOURCES / 'fin3-xbrl.html'
fin4 = RESOURCES / 'fin4-xbrl.html'
micro_accounts = RESOURCES / 'micro-accounts-xbrl.html'


with open(fin4, encoding="utf8") as file:
    x = IXBRL(file)

# print(x.to_table())
# print(json.dumps(x.to_table(), indent=4))
# print(x.schema)
# print(json.dumps(x.namespaces, indent=4))
# print()

# print("contexts")
# print("--------")
# for i in x.contexts:
#     print(i, x.contexts[i].__dict__)
# print()

# print("units")
# print("-----")
# for i in x.units:
#     print(i, x.units[i])
# print()

# print("nonnumeric")
# print("----------")
# for i in x.nonnumeric:
#     print(i.__dict__)
# print()

# TODO: transform numeric to a pandas DF,
#  text = value as text (not required),
#  name = type of fin (required),
#  unit = currency (required),
#  value = value (required),
#  there might be something in context, or format objects that specify if value in 1000's

print("numeric")
print("-------")
for i in x.numeric:
    print(i.__dict__)
print()