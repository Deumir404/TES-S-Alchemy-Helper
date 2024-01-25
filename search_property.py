# coding: UTF-8
import json

def Search_by_property(text):
        dict = []
        with open("ingredient1.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict.append(json.loads(file_content))
        correct_items = []
        for i in range(len(dict[0])):
                list_propetries = dict[0][i].get("properties_json")
                for j in range(4):
                        list_propetries[j] = list_propetries[j].lower()
                if text.lower() in list_propetries :
                        correct_items.append(dict[0][i].get("name_ingredient"))
        if len(correct_items) == 0 :
                return ("Ингредиенты не найдены")
        else :
                return correct_items