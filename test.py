import json

def Search_by_property(text):
        dict_1 = []
        list_dict = []
        with open("poison_with_tag.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        power = 100
        for i in range(len(dict_1[0])):
            list = dict_1[0][i].get("description").split("{power}")
            if len(list) == 2:
                string = list[0] + str(power) + list[1]
            else :
                  string =list
            print(string)
            

Search_by_property(1)