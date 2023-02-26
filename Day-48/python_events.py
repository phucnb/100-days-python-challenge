from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service = Service('/Users/phucnb/chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org")
event_widget = driver.find_element(By.CSS_SELECTOR, 'div.event-widget')
li_menu = event_widget.find_elements(By.TAG_NAME, 'li')
event_dict = {li_menu.index(li) : {'time' : li.find_element(By.TAG_NAME, 'time').text, 'name' : li.find_element(By.TAG_NAME, 'a').text} for li in li_menu}
print(event_dict)
driver.quit()