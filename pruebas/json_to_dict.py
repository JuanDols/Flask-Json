import json

''' file: bd.json cada línea siendo un objecto
{"id":"hola",...}
{"id":"adios",...}
{"id":"holaadios",...}
'''

def load_json_from(file):
    file = open(file, "r")
    contents = file.readlines()
    file.close()
    dict_array = []
    for element in contents:
        dict_array.append(json.loads(element))
    return dict_array