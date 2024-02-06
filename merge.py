# coding: UTF-8
#1 - провизор
#2 - отравитель
#3 - провизор + целитель

import json

def write_json(data, filename= 'merge_alchemy.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def merge():
        dict_1 = []
        dict_2 = []
        list_dict = []
        with open("poison_basic.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        for i in range(len(dict_1[0])):
                name = dict_1[0][i].get("name_potion")
                properties = dict_1[0][i].get("description")
                tag1 = dict_1[0][i].get("tag")
                power1 = dict_1[0][i].get("power")
                data = dict(name_potion = name, description = properties, tag = tag1, power = int(power1))
                print(data)
                list_dict.append(data)
        
        with open("potion_basic.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_2.append(json.loads(file_content))
        for i in range(len(dict_2[0])):
                name = dict_2[0][i].get("name_potion")
                properties = dict_2[0][i].get("description")
                tag1 = dict_2[0][i].get("tag")
                power1 = dict_2[0][i].get("power")
                data = dict(name_potion = name, description = properties, tag = tag1, power = int(power1))
                print(data)
                list_dict.append(data)
        write_json(list_dict)
                


merge()