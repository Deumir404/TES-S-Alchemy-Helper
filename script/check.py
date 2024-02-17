# coding: UTF-8
#1 - провизор
#2 - отравитель
#3 - провизор + целитель

import json

def write_json(data, filename= 'merge_alchemy.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def check():
        dict_1 = []
        with open("alchemy_with_tags.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        for i in range(len(dict_1[0])):
            name = dict_1[0][i].get("name_potion")
            duration = dict_1[0][i].get("base_duration")
            if duration != 0:
                print(name + " " + str(i))
        
        
check()