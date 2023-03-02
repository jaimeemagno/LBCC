from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_ojb=Service("/Users/ayahtekmba/Downloads/chromedriver")
driver=webdriver.Chrome(service=serv_ojb)

driver.get("https://lbcoop-uat-admin.lakasbayanihancreditcoop.com/")

driver.find_element(By.NAME,"username").send_keys("superqa@yopmail.com")
driver.find_element(By.ID,"psswrd").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
driver.find_element(By.LINK_TEXT,"Share Capital"). click()



act_title=driver.title
exp_title="Share Capital"

if act_title==exp_title:
    print("Passed")
else:
    print("Failed")

driver.close()