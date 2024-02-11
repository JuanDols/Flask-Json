import json
from json_to_array import *

def get_uniq_keys(data, key):
    keys = []

    for element in data:
        if element[key] not in keys:
            keys.append(element[key])
    return keys       

def group_by_uniq_keys(data, key, group_by):
    new_dict = {}

    for identifier in group_by:
        new_dict[identifier] = []

    for element in data:
        array = new_dict[element[key]]
        array.append(element)
        new_dict[element[key]] = array

    return new_dict

def order_by_helpful(data, helpful_id):

    list_of_keys = data.keys()

    new_dict = {}

    for key in list_of_keys:

        for review in data[key]:
            
            helpful_key = str(review[helpful_id][0] - review[helpful_id][1])
            
            if helpful_key in new_dict.keys():
                new_dict[helpful_key].append(review)
            else:
                new_dict[helpful_key] = [review]

    return new_dict
            

array_dicts=load_json_from('bd.json')

uniq_keys = get_uniq_keys(array_dicts, 'asin')

grouped_by_id = group_by_uniq_keys(array_dicts, 'asin', uniq_keys)

order_by_helpful(grouped_by_id, 'helpful')