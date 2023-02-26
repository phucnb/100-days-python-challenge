from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service('/Users/phucnb/chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys("Python")
search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys(Keys.ENTER)
