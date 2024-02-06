# coding: UTF-8
import json

import json

def get_description(text, lvl, alchemy, healer,farma,poison):
        dict_1 = []
        with open("merge_alchemy.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        for i in range(len(dict_1[0])):
            if text.lower() == dict_1[0][i].get("name_potion").lower():
                list = dict_1[0][i].get("description").split("{power}")
                tag = dict_1[0][i].get("tag")
                print(tag)
                basic = dict_1[0][i].get("power")
                power = math_stat(tag, basic, lvl, alchemy, healer, farma, poison)
                if len(list) == 2:
                    description = list[0] + str(power) + list[1]
                else :
                    description = list[0]
                return description

    
def math_stat(tag, num, lvl, alchemy, healer,farma,poison):
    if tag == 1:
        answer = round((num + round(lvl/10)) * (1 + 0.2 * alchemy) * (1 + 0.25 *farma))
    if tag == 3:
        answer = round((num + round(lvl/10)) * (1 + 0.2 * alchemy) * (1 + 0.25 *farma) * (1 + 0.25 * healer))
    if tag == 4:  
        answer = round((num + round(lvl/12.3)) * (1 + 0.2 * alchemy) * (1 + 0.25 *farma))
        #недоработан
    if tag == 5:
        answer = round((num + round(lvl/50)) * (1 + 0.2 * alchemy) * (1 + 0.25 *farma))
    if tag == 6:
        answer = round((num + round(lvl/25)) * (1 + 0.2 * alchemy) * (1 + 0.25 *farma))
    if tag == 7:
        answer = round((num + round(lvl/12,3)) * (1 + 0.2 * alchemy))
        #недоработан
    if tag == 8:
        answer = round((num + round(lvl/50)) * (1 + 0.2 * alchemy))
    if tag == 9:
        answer = round((num + round(lvl/50)) * (1 + 0.2 * alchemy) * (1 + 0.25 *poison))
    if tag == 10:
        answer = round((num + round(lvl/25)) * (1 + 0.2 * alchemy) * (1 + 0.25 *poison))
    if tag == 11:
        answer = round((num + round(lvl/12,3)) * (1 + 0.2 * alchemy))
        #недоработан
    if tag == 12:
        answer = round((num + round(lvl/12,3)) * (1 + 0.2 * alchemy) * (1 + 0.25 *poison))
        #недоработан
    if tag == 2:
        answer = round((num + round(lvl/10)) * (1 + 0.2 * alchemy) * (1 + 0.25 *poison))
    return answer 
     
#1 - 16 10 - 17 20 - 18 30 - 18 40 - 19 50 - 20 60 - 21 70 - 22 80 - 22 90 -23 100 - 24


            
