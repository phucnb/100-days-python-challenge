import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
service = Service('/Users/phucnb/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/Users/phucnb/Library/Application Support/Google/Chrome/')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://tinder.com/app/recs')

time.sleep(3)
try:
    while True:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
except Exception as e:
    print(e)
    driver.quit()