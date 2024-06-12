from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(1)
driver.maximize_window()
time.sleep(1)

searchInput = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button').click()
time.sleep(1)

searchInput = driver.find_element(By.XPATH, '//*[@id="query-builder-test"]')

searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(4)

result = driver.find_element(By.XPATH, "").find_element()
#for dongusunu çalıştır

for element in result:
    print(element.text)

driver.close()
