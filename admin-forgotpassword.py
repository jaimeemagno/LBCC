from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_ojb=Service("/Users/ayahtekmba/Downloads/chromedriver")
driver=webdriver.Chrome(service=serv_ojb)

driver.get("https://lbcoop-uat-admin.lakasbayanihancreditcoop.com/")

driver.find_element(By.LINK_TEXT,"Forgot Password"). click()
driver.find_element(By.ID,"cemail").send_keys("superqa@yopmail.com")
driver.find_element(By.ID,"btn-forgot").click()


act_title=driver.title
exp_title="Forgot Password"

if act_title==exp_title:
    print("Passed")
else:
    print("Failed")

driver.close()