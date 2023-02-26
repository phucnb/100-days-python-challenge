from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

TIMEOUT_DURATION = 60 * 5   # Seconds
VERIFICATION = 5        # Seconds
service = Service('/Users/phucnb/chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

language_select = driver.find_element(By.ID, "langSelect-EN")
language_select.click()

time.sleep(3)

while True:
    products = driver.find_element(By.ID, 'products')
    product = products.find_elements(By.CLASS_NAME, 'unlocked')
    if product:
        # product[-1].click()
        product[-1].click()
    else:
        print("locked")    
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()