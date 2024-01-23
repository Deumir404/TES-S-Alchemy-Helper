import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def write_json(data, filename= 'ingredient1.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_url(url):
    clm = [4 , 5, 6, 7]
    option1 = webdriver.ChromeOptions()
    option1.add_argument("--headless=new")
    option1.add_argument("--ignore-ssl-errors")
    option1.add_argument("--ignore-cerificate-errors")

    driver = webdriver.Chrome(options=option1)
    driver.get(url)
    driver.implicitly_wait(10)
    #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr
    #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[1]/tbody/tr
    #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[2]/tbody/tr
    path = "/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr"
    rows = len(driver.find_elements(by=By.XPATH, value = path))
    print(rows)
    list_dict = []
    for r in range(2, rows+1):
        name = driver.find_element(by=By.XPATH, value = path+ '[' + str(r)+']/td[2]').text
        properties = []
        for c in clm:
            properties.append(driver.find_element(by=By.XPATH, value = path + '['+str(r)+']/td['+str(c)+']').text)
        data = dict(name_ingredient = name, properties_json = properties)
        list_dict.append(data)
        print("complete "+str(r))
    write_json(list_dict)

def main():
    
        url = "https://elderscrolls.fandom.com/ru/wiki/%D0%98%D0%BD%D0%B3%D1%80%D0%B5%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D1%8B_(Skyrim)?so=search"
        get_url(url)
        print("Complete")
        

main()