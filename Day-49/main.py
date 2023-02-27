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
# EMAIL = os.environ.get('EMAIL')
# PASSWORD = os.environ.get('PASSWORD')

# driver.get("https://www.linkedin.com")
# username = driver.find_element(By.ID, 'session_key')
# username.send_keys(EMAIL)
# password = driver.find_element(By.ID, 'session_password')
# password.send_keys(PASSWORD)
# password.send_keys(Keys.ENTER)
# time.sleep(3)
driver.get("https://www.linkedin.com/jobs")
most_recent_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'jobs-home-soho-search-card__link-wrapper'))
    )
print(most_recent_search.find_element(By.CLASS_NAME, 'tvm__text--positive').text)
# most_recent_search.click()
url=most_recent_search.get_attribute(f'href')
# with open('job.html', 'w') as file:
#     file.write(driver.page_source)
try:
    for page in range(0, 1000, 25):
        
        driver.get(f'{url}&start={page}')
        time.sleep(3)
        results_list__title = driver.find_element(By.ID, 'results-list__title')
        print(results_list__title.get_attribute('title'))

        ActionChains(driver).move_to_element(driver.find_element(By.CLASS_NAME, 'artdeco-pagination__pages--number')).perform()
        jobs_result = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
        for job in jobs_result:
            ActionChains(driver).move_to_element(job).perform()
            job.click()
            time.sleep(0.5)
            job_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jobs-unified-top-card__job-title'))
            )
            print(job_title.text)
            company_tag = driver.find_element(By.CLASS_NAME, 'jobs-unified-top-card__subtitle-primary-grouping')
            company_name = company_tag.find_element(By.CLASS_NAME, 'jobs-unified-top-card__company-name')
            print(company_name.text)
            # print(company_name.get_attribute('href'))
            try:
                company_location = company_tag.find_element(By.CLASS_NAME, 'jobs-unified-top-card__bullet')
                company_type = company_tag.find_element(By.CLASS_NAME, 'jobs-unified-top-card__workplace-type')
                print(company_location.text)
                print(company_type.text)
            except:
                continue
            print('----------------------------')

except Exception as e:
    print(e)
    # driver.quit()




