from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import re
driver = webdriver.Chrome('C:\\Users\\Z\\Downloads\\chromedriver.exe')
wait = WebDriverWait(driver, 600)
driver.get("http://linkedin.com")
input()
buttons = driver.find_elements_by_class_name("search-result__actions--primary")
for B in buttons:
    print(B.get_attribute("innerHTML"))