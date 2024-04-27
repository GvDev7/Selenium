from selenium import webdriver
from selenium.webdriver.chrome.service  import Service

# Webdriver is an automation tool that can control Google Chrome
service = Service(executable_path="")
driver = webdriver.Chrome(service=service)