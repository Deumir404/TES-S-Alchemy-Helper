# coding: UTF-8
#1 - провизор
#2 - отравитель
#3 - провизор + целитель

import json

def write_json(data, filename= 'alchemy_with_tags.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def merge():
        dict_1 = []
        dict_2 = []
        list_dict = []
        with open("alchemy_with_base.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        with open("merge_alchemy.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_2.append(json.loads(file_content))
        for i in range(len(dict_1[0])):
                name = dict_1[0][i].get("name_potion")
                base_cost1 = dict_1[0][i].get("base_cost")
                base_power1 = dict_1[0][i].get("base_power")
                power1 = dict_1[0][i].get("base_duration")
                for j in range(len(dict_2[0])):
                  name2 = dict_2[0][j].get("name_potion")
                  if name == name2:
                        description1 = dict_2[0][j].get("description")
                        tag1 = dict_2[0][j].get("tag")
                data = dict(name_potion = name, description = description1, tag = tag1, base_cost = float(base_cost1), base_power = int(base_power1), base_duration = int(power1))
                print(data)
                list_dict.append(data)
                
        
        write_json(list_dict)
                


merge()