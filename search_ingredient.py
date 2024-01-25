import json

def search_by_ingredient(text):
        dict = []
        with open("ingredient1.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict.append(json.loads(file_content))
        item = []
        for i in range(len(dict[0])):
                if text.lower() == dict[0][i].get("name_ingredient").lower() :
                        item.append(dict[0][i].get("name_ingredient"))
                        item.append(dict[0][i].get("properties_json"))
        if len(item) == 0 :
                return ("Ингредиент не найден")
        else :
                return item