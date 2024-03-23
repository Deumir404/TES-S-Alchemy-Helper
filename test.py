import json
import random

def get_property():
    dict_property = []
    with open("res/alchemy_with_tags.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_property.append(json.loads(file_content))
    result = random.choice(dict_property[0])
    return result.get("name_potion")