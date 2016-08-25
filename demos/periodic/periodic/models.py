"""periodic Models."""
import json


print('Loading data...', end='')

with open('periodic/data.json') as data_file:
    ELEMENTS = json.load(data_file)

SYMBOL_TO_ELEMENT = {
    element['symbol']: element
    for element
    in ELEMENTS
}

print('done')
