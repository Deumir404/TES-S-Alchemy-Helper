# coding: UTF-8
import json
import math
from search_ingredient import search_by_ingredient





def get_healer(tag):
    if tag == 3:
        return 1
    else:
        return 0
def get_farma(tag):
    list = [1,3,4,5,6]
    if tag in list:
        return 1
    else:
        return 0
def get_poison(tag):
    list = [2,9,10,12]
    if tag in list:
        return 1
    else:
        return 0    
def math_power(tag, lvl, alchemy, healer,farma,poison):
    #* (1 + fortifyAlchemy/100)
    healer_perk = get_healer(tag)
    farma_perk = get_farma(tag)
    poison_perk = get_poison(tag)
    power = 4 * (1 +  lvl / 200)  * (1 + alchemy * 0.2) * (1 + healer * healer_perk * 0.25) * (1 + farma * farma_perk * 0.25 + poison * poison_perk * 0.25)
    return power
def get_description(text, lvl, alchemy, healer,farma,poison):
        dict_1 = []
        with open("res/alchemy_with_tags.json", 'r', encoding= "UTF-8") as file:
                file_content = file.read()
                dict_1.append(json.loads(file_content))
        for i in range(len(dict_1[0])):
            if text.lower() == dict_1[0][i].get("name_potion").lower():
                list = dict_1[0][i].get("description").split("{power}")
                list_dur = dict_1[0][i].get("description").split("{dur}")
                tag = dict_1[0][i].get("tag")
                basic_power = dict_1[0][i].get("base_power")
                basic_duration = dict_1[0][i].get("base_duration")
                basic_cost = dict_1[0][i].get("base_cost")
                mult_power = math_power(tag, lvl, alchemy, healer, farma, poison)
                if len(list) == 2:
                    power = round(basic_power * mult_power)
                    duration = basic_duration
                    description = list[0] + str(power) + list[1]
                else :
                    if len(list_dur) == 2:
                        power = round(basic_power * mult_power)
                        duration = round(basic_duration* mult_power)
                        description = list_dur[0] + str(duration) + list_dur[1]
                    else:
                        power = round(basic_power * mult_power)
                        duration = round(basic_duration* mult_power)
                        description = list_dur[0]
                if power == 0:
                    Gold_cost = math.trunc( basic_cost *  ((duration/10)**1.1) )
                elif duration == 0:
                    Gold_cost = math.trunc( basic_cost *  (power**1.1) )
                else:
                    Gold_cost = math.trunc( basic_cost *  (power**1.1) * ((duration/10)**1.1) )
                answer = []
                answer.append(description)
                answer.append(Gold_cost)
                return answer

def sort_comparator(list):
    return list[1]
def get_amount(list, name):
    #есть баг
    sort_list = []
    for i in range(len(list)):
        list_property = search_by_ingredient(list[i][0])
        for j in range(4):
            if list_property[1][j] == name:
                sort_list.append(list[i])
    sort_list.sort(key=sort_comparator)
    sum = 0
    for i in range(len(sort_list)-1):
        if sort_list[i+1][1] - sort_list[i][1] >= 0:
            sort_list[i+1][1] - sort_list[i][1]
            sum += sort_list[i][1]
        else:
            return sum
    return sum  

     
#1 - 16 10 - 17 20 - 18 30 - 18 40 - 19 50 - 20 60 - 21 70 - 22 80 - 22 90 -23 100 - 24


            
