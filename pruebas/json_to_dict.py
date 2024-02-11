import json

''' file: bd.json cada línea siendo un objecto
{"id":"hola",...}
{"id":"adios",...}
{"id":"holaadios",...}
'''

file = open("bd.json", "r")
contents = file.readlines()
file.close()


for element in contents:
    python_dict = json.loads(element)
    print(python_dict['asin'])