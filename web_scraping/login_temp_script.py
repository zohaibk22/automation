import chrome_driver
from selenium.webdriver.common.keys import Keys
import time

def main():
    driver = chrome_driver.init_chrome_driver('https://automated.pythonanywhere.com/login/')
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    print(driver.current_url)
    temp = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    
    return temp.text.split(": ")[1]
    
    
print(main())