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
        # with open("ingredients2.json", 'r', encoding= "UTF-8") as file:
        #         file_content = file.read()
        #         dict.append(json.loads(file_content))
        for i in range(1):
            url = "https://static.wikia.nocookie.net/elderscrolls/images/0/03/%D0%90%D0%BB%D1%8B%D0%B9_%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D1%8C_%D0%9D%D0%B8%D1%80%D0%BD%D0%B0_%28Skyrim%29.png/revision/latest?cb=20130220201551&path-prefix=ru"
            name = "Алый корень Нирна"
            driver.get(url)
            driver.implicitly_wait(30)
            time.sleep(3)
            #driver.execute_script("arguments[0].removeAttribute('style')", row)
            image = driver.find_element(By.XPATH, value =" /html/body/img")
            image.screenshot(f"res/image/{name}.png")
        driver.close()
        print("Complete")

get_image()