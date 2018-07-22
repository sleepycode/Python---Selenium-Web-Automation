from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import re
driver = webdriver.Chrome('C:\\Users\\Z\\Downloads\\chromedriver.exe')
wait = WebDriverWait(driver, 600)
driver.get("http://uzomoney.site/showadv.php?rstr=0.2909693985777466")
driver.find_element_by_id("username").send_keys("746it14")
driver.find_element_by_id("password").send_keys("qwerty")
driver.find_element_by_id("password").send_keys(Keys.TAB+Keys.ENTER)
input()
while True:
    mainform = driver.find_element_by_name("mainf")
    info = mainform.get_attribute("innerHTML")
    imgs = info.split(".png")
    ans= imgs[0][-1]+imgs[1][-1]+imgs[2][-1]+imgs[3][-1]
    inputbox = driver.find_element_by_name("capcha")
    inputbox.send_keys(ans + Keys.ENTER)
