import json

print("Введите название ингредиента")
text = input()
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
        print("Ингредиент не найден")
else :
        print(item[0])
        print(item[1])