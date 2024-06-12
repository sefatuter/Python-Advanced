from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
# driver = webdriver.Chrome(options=options)


# driver.get("https://www.w3schools.com/")


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/sadikturan"
driver.get(url)

print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)

driver.close()

