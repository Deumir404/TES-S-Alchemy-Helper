import json
import random
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

def get_property():
    dict_property = []
    with open("res/alchemy_with_tags.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_property.append(json.loads(file_content))
    result = random.choice(dict_property[0])
    return result.get("name_potion")

def count_above_one(dict):
    count = 0
    for i in range(len(dict)):
        if dict[i]["sum"] > 1:
            count += 1
    return count

def add_property(list, dict_for_write):
    if len(dict_for_write) == 0 :
        list_property = []
    else :
        list_property = []
        for i in range(len(dict_for_write)):
            if dict_for_write[i]["name"] not in list_property:
                list_property.append(dict_for_write[i]["name"])
    for j in range(4):
                dict_item = dict(name = list[1][j], sum = 1)
                if list[1][j] not in list_property:
                    list_property.append(list[1][j])
                    dict_for_write.append(dict_item)
                else:
                    for k in range(len(dict_for_write)):
                        if dict_for_write[k]["name"] == dict_item["name"]:
                            dict_for_write[k]["sum"] =  dict_for_write[k]["sum"] + 1
                            break

def load_file(list_for_write, Table):
    try :
        list_file = []
        with open("inventory.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                list_file = json.loads(file_content)
        list_for_write.clear()
        for i in range(len(list_file)):
            list_for_write.append(list_file[i])
        Table.update_table(list_for_write)
    except FileNotFoundError :
        Error_message = QDialog()
        Message_text = QLabel("Ошибка при загрузке файла")
        Button_OK = QPushButton("ОК")
        layout_message = QVBoxLayout()
        layout_message.addWidget(Message_text)
        layout_message.addWidget(Button_OK)
        Error_message.setLayout(layout_message)
        Button_OK.clicked.connect(Error_message.accept)
        Error_message.exec()
    
def save_file(list_inv):
    with open("inventory.json", 'w', encoding= "UTF-8") as file:
        json.dump(list_inv, file, indent=2, ensure_ascii=False)