from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_ojb=Service("/Users/ayahtekmba/Downloads/chromedriver")
driver=webdriver.Chrome(service=serv_ojb)

driver.get("https://lbcoop-uat-member.lakasbayanihancreditcoop.com/")

driver.find_element(By.NAME,"username").send_keys("xexessojubru-5640@yopmail.com")
driver.find_element(By.ID,"psswrd").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()


act_title=driver.title
exp_title="Dashboard"

if act_title==exp_title:
    print("Passed")
else:
    print("Failed")

driver.close()