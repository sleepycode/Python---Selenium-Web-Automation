from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import string
import re
driver = webdriver.Chrome('C:\\Users\\Z\\Downloads\\chromedriver.exe')
wait = WebDriverWait(driver, 600)
driver.get("http://gmail.com")
id = driver.find_element_by_id("identifierId")
id.send_keys("kshitiznsit"+Keys.ENTER)
time.sleep(1)
currpswd = "UqpgWcN7KdVR"
passw = driver.find_element_by_name("password")
passw.send_keys(currpswd + Keys.ENTER)
count = 0
while count<200:
    count +=1
    time.sleep(5)
    driver.get("https://accounts.google.com/signin/v2/sl/pwd?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fhl%3Den&followup=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fhl%3Den&hl=en&emr=1&mrp=security&rart=ANgoxce6adSEJnn-bFYr8Sxh_2sCGgN8DV1MuS8fbboqnXkjFl6XqE2Mr_8WsumRnXRZ-e2Arq3TwCE_ZEIa6g_7vpHZKgT3fA&authuser=0&csig=AF-SEnZbbp12rQ5Sk-Wy%3A1529817571&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    passw = driver.find_element_by_name("password")
    passw.send_keys(currpswd + Keys.ENTER)
    newpswd = ''.join(random.choice(string.ascii_uppercase + string.digits +string.ascii_lowercase) for _ in range(12))
    print("currpswd = " + currpswd + "\nnewpswd = " + newpswd + "\n--------------------------------\n" )
    time.sleep(2)
    passw = driver.find_element_by_name("password")
    passw.send_keys(newpswd)
    passw = driver.find_element_by_name("confirmation_password")
    passw.send_keys(newpswd + Keys.ENTER)
    currpswd = newpswd

