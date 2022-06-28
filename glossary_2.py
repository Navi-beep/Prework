from multiprocessing.sharedctypes import Value


glossary_list = {
    'int': 'integer',
    'string': 'sequence of characters',
    'key': 'indexes of a list', 
    'value': 'a letter or number',
    'variable': "stores a value in a program",
    'boolean': 'binary variable, two possible values true and false',
    'tuple': 'list of values that cannot be changed',
    'sum': 'total amount', 
    'range': 'returns a sequence of numbers starting from zero and incrementing by 1 and stops before the given number',
    'list': 'stores collections of data',
    }

for key, value in glossary_list.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")