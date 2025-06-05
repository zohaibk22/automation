import chrome_driver
import time

def text_cleanup(text):
    """_summary_

    Args:
        text (_type_):string _description_
        extracts temperature value from string 
    """
    
    split_string = float(text.split(": "))
    return split_string[1]


def main():
    driver = chrome_driver.init_chrome_driver("https://automated.pythonanywhere.com/")
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return text_cleanup(element.text)

print(main())

if __name__ == '__main__':
    print(main())