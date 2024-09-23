import chrome_driver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = chrome_driver.init_chrome_driver('https://titan22.com/')
    account = driver.find_element(by='xpath', value='/html/body/header/div[1]/div[1]/div/div[3]/a[2]').click()
    time.sleep(2)
    email = driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[1]/input').send_keys('zohaibk1022@gmail.com')
    password = driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[2]/input').send_keys('Blue1997!')
    button = driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/button').click()
    time.sleep(10)

main()