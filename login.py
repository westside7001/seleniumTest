from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver import Actions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get('https://mygoldenqa.arlo.com/#/home')
signIn = driver.find_element(By.CLASS_NAME,'mdc-button__label')
signIn.click()

driver.get('https://mygoldenqa.arlo.com/#/login')
waitLogin = WebDriverWait(driver, 10)
element = waitLogin.until(EC.presence_of_element_located((By.ID, 'loginForm')))
loginForm = driver.find_element(By.ID,'loginForm')
driver.find_element(By.ID, 'loginEmail').send_keys('arloqaregister+1701127729525jwrn+us@gmail.com')
driver.find_element(By.ID, 'loginPassword').send_keys('Netgear1')
loginButton = driver.find_element(By.ID,'loginForm')
loginButton.submit()
time.sleep(15)

#接下來要做功能測試，像是DashBoard上的mode change，更改rule，新增schedule和Geofence，location的設定
driver.close()