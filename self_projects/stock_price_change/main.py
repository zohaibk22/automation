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
    ]:
        try:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            break
        except TimeoutException:
            pass
def main():
    url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'
    driver = init_driver(url)
    time.sleep(2)
    dismiss_consent_if_any(driver)
    percentage = driver.find_element(by='xpath', value='/html/body/div[1]/div/section[1]/div/div/div[2]/span[2]')
    print(percentage, "TXT")

    

if __name__ == '__main__':
    main()