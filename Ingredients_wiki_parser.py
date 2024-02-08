import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


def write_json(data, filename= 'potion.json'):
    with open(filename, 'a+', encoding= "UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_url(url):
    # try :
        option1 = Options()
        option1.add_argument("--headless")
        

        driver = webdriver.Firefox(options= option1)
        driver.get(url)
        driver.implicitly_wait(30)
        #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr
        #/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/tbody/tr
        #/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/tbody/tr[1]/th/a
        #/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/tbody/tr[1]/td[1]
        #/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/thead/tr[1]/th/span
        #driver.find_element(By.XPATH, value = "/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/thead/tr[1]/th/span").click()
        path = "/html/body/div[5]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[1]/table[5]/tbody/tr"
        rows = len(driver.find_elements(By.XPATH, value = path))
        print(rows-1)
        row = driver.find_element(By.XPATH, value = path+ '[2]')
        driver.execute_script("arguments[0].removeAttribute('style')", row)
        list_dict = []
        for r in range(1, rows-1):
            row = driver.find_element(By.XPATH, value = path+ '['+ str(r)+']')
            driver.execute_script("arguments[0].removeAttribute('style')", row)
            name = driver.find_element(By.XPATH, value = path+ '['+ str(r)+']/th').text
            properties = str()
            
            properties = driver.find_element(By.XPATH, value = path + '['+str(r)+']/td[1]').text
            data = dict(name_potion = name, description = properties)
            print(data)
            list_dict.append(data)
            print("complete "+str(r))
        write_json(list_dict)
        driver.close()
    # except :
    #     print("error")
    #     driver.close()

def main():
    
        url = "https://elderscrolls.fandom.com/ru/wiki/%D0%90%D0%BB%D1%85%D0%B8%D0%BC%D0%B8%D1%8F_(Skyrim)#%D0%9F%D1%80%D0%B8%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B7%D0%B5%D0%BB%D0%B8%D0%B9"
        get_url(url)
        print("Complete")
        

main()