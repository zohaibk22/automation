import chrome_driver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


def logger(func):
    def test(*args, **kwargs):
        
        print('script done')
        return func(*args, **kwargs)
    
    return test


@logger
def write_to_file(text):
    filename = f"{datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = chrome_driver.init_chrome_driver("https://automated.pythonanywhere.com/")

    while True:
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        write_to_file(element.text)
        


main()