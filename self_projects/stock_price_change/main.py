from utils import init_driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def dismiss_consent_if_any(driver):
    for xpath in [
        "//button[normalize-space()='Accept']",
        "//button[contains(., 'Accept all')]",
        "//button[contains(., 'I agree')]",
        "//button[contains(., 'Got it')]",
         "//button[contains(., 'Allow all cookies')]",
    ]:
        
        try:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            break
        except TimeoutException:
            pass
def main():
    url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'
    driver = init_driver(url)
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Allow all cookies')]"))
        )
        cookies_button.click()
    except Exception as e:
        print("Cookies button not found or not clickable:", e)
    element = driver.find_element(by='class name', value='stock-trend')
    percentage = element.text
    full_class_name = element.get_attribute('class')
    if 'trend-drop' in full_class_name:
        percentage = float(percentage.replace('%', '').strip())
        # Need to enter email script here

    

if __name__ == '__main__':
    main()