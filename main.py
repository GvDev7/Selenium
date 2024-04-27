from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
# Needed to search elements in the html
from selenium.webdriver.common.by import By
# Needed to interact with searched element
from selenium.webdriver.common.keys import Keys
import time

# Webdriver is an automation tool that can control Google Chrome
# Download webdriver at https://sites.google.com/chromium.org/driver/
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Grabbing the search element  by its name, id or class
search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys("Python" + Keys.ENTER)

time.sleep(20)


driver.quit()