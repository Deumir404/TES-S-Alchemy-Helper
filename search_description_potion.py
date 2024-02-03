# coding: UTF-8
import json

def Search_by_name_potion(text):
        dict = []
        with open("potion.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict.append(json.loads(file_content))
        answer = "Описание не найдено"
        for i in range(len(dict[0])):
                name = dict[0][i].get("name_potion")
                if text.lower() == name.lower() :
                        answer = dict[0][i].get("description")
        return answer

def Search_by_name_poison(text):
        dict = []
        with open("poison.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict.append(json.loads(file_content))
        answer = "Описание не найдено"
        for i in range(len(dict[0])):
                name = dict[0][i].get("name_potion")
                if text.lower() == name.lower() :
                        answer = dict[0][i].get("description")        
        return answer