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
driver.find_element(By.ID, 'loginEmail').send_keys('arloqaregister+1701222479917eyzy+us@gmail.com')
driver.find_element(By.ID, 'loginPassword').send_keys('Netgear1')
loginButton = driver.find_element(By.ID,'loginForm')
loginButton.submit()
time.sleep(15)

feed = driver.find_element(By.ID,'automation_action_nav_feed')
feed.click()
print('feed')
time.sleep(5)
closefeed = driver.find_element(By.CLASS_NAME,'close')
closefeed.click()

er = driver.find_element(By.ID,'automation_action_nav_emergency_response')
er.click()
print('Emergency Response')
time.sleep(5)

devices = driver.find_element(By.ID,'automation_action_nav_cameras_new')
devices.click()
print('Devices')
time.sleep(5)
closeUpdatedDevices = driver.find_element(By.CLASS_NAME,'close')
closeUpdatedDevices.click()

Routines = driver.find_element(By.ID,'automation_action_nav_routines.modes')
Routines.click()
print('Routines')
time.sleep(5)
closeRoutines = driver.find_element(By.CLASS_NAME,'close')
closeRoutines.click()

Settings = driver.find_element(By.ID,'automation_action_nav_settings')
Settings.click()
print('Settings')
time.sleep(5)

logOut = driver.find_element(By.CLASS_NAME,'btn-full-width-red')
logOut.click()
driver.quit()
#接下來要做功能測試，像是DashBoard上的mode change，更改rule，新增schedule和Geofence，location的設定
