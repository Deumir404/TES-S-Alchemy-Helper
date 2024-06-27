# coding: UTF-8
#1 - провизор
#2 - отравитель
#3 - провизор + целитель

import json

def write_json(data, filename= 'ingredients_full.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def merge():
        dict_for_write = []
        dict_for_read = []
        lenght = 0
        for i in range(3):
                if i == 0 : continue
                with open(f"ingredients{i}.json", 'r', encoding= "UTF-8") as file:
                        file_content = file.read()
                        dict_for_read.append(json.loads(file_content))
                lenght += len(dict_for_read[0])
                print(lenght)
                for j in range(len(dict_for_read[0])):
                        name = dict_for_read[0][j].get("name_ingredient")
                        prop = dict_for_read[0][j].get("properties_json")
                        data = dict(name_ingredient = name, properties_json = prop)
                        dict_for_write.append(data)
                dict_for_read.clear()
                
        print(lenght)
        print(len(dict_for_write))
        write_json(dict_for_write)

                


merge()