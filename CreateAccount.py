#Create Account已寫完，因為卡在Account 認證的部份，所以就只寫到把Create Account 資料填完即結束
#往後可新增檢查ToS的日期，已確認是否為最新版

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get("https://mygoldenqa.arlo.com/#/home")
CreateAcct = driver.find_element(By.CLASS_NAME,'basic-link')
CreateAcct.click()

driver.get('https://mygoldenqa.arlo.com/#/registration')
driver.implicitly_wait(3)
ToSCheck = driver.find_element(By.LINK_TEXT,'Terms of Service')
ToSCheck.click()
time.sleep(5)
goBack = driver.find_element(By.CLASS_NAME,'mdc-button__label')
goBack.click()
driver.find_element(By.ID, 'firstNameArlo').send_keys('Smart')
driver.find_element(By.ID, 'lastNameArlo').send_keys('AI')
driver.find_element(By.ID, 'emailArlo').send_keys('chsu7001+1@gmail.com')
driver.find_element(By.ID, 'confirmEmailArlo').send_keys('chsu7001+1@gmail.com')
driver.find_element(By.ID, 'passwordArlo').send_keys('Netgear1')
driver.find_element(By.ID, 'confirmPasswordArlo').send_keys('Netgear1')

commercialBox  = driver.find_element(By.ID, 'mat-mdc-checkbox-3-input')
if commercialBox.is_selected():
    commercialBox.click()
    print('commercialBox unchecked')

ToSBox = driver.find_element(By.ID, 'termsAndConditionsArlo-input')
ToSBox.click()

time.sleep(3)
driver.close()
