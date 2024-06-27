import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


def get_image():
    # try :
        option1 = Options()
        #option1.add_argument("--headless")
        
        dict = []
        driver = webdriver.Firefox(options= option1)
        with open("ingredients5.json", 'r', encoding= "UTF-8") as file:
                 file_content = file.read()
                 dict.append(json.loads(file_content))
        for i in range(len(dict[0])):
            name = dict[0][i].get("name_potion")
            url = dict[0][i].get("image")
            driver.get(url)
            driver.implicitly_wait(30)
            time.sleep(3)
            #driver.execute_script("arguments[0].removeAttribute('style')", row)
            image = driver.find_element(By.XPATH, value =" /html/body/img")
            image.screenshot(f"res/image/{name}.png")
        driver.close()
        print("Complete")

get_image()