from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get("https://mygoldenqa.arlo.com/#/home")
CreateAcct = driver.find_element(By.CLASS_NAME,'basic-link')
#driver.find_element(By.ID, "loginEmail").send_keys("arloqaregister+1701127729525jwrn+us@gmail.com")
#driver.find_element(By.ID, "loginPassword").send_keys("Netgear1")
#signInButton = driver.find_element(By.CLASS_NAME,"login-button-home")
CreateAcct.click()
#wait
driver.get('https://mygoldenqa.arlo.com/#/registration')
driver.implicitly_wait(3)

#driver.find_element(By.ID, 'firstNameArlo').send_keys('Smart')
#driver.find_element(By.ID, 'lastNameArlo').send_keys('AI')
#driver.find_element(By.ID, 'emailArlo').send_keys('chsu7001+1@gmail.com')
#driver.find_element(By.ID, 'confirmEmailArlo').send_keys('chsu7001+1@gmail.com')
#driver.find_element(By.ID, 'passwordArlo').send_keys('Netgear1')
#driver.find_element(By.ID, 'confirmPasswordArlo').send_keys('Netgear1')
commercialBox  = driver.find_element(By.ID, 'mat-mdc-checkbox-3-input')
if commercialBox.is_selected():
    commercialBox.click()
    print('commercialBox unchecked')

ToSBox = driver.find_element(By.ID, 'termsAndConditionsArlo-input')
ToSBox.click()

ToSCheck = driver.find_element(By.LINK_TEXT,'Terms of Service')
ToSCheck.click()
time.sleep(5)
goBack = driver.find_element(By.CLASS_NAME,'mdc-button__label')
goBack.click()
#submitButton = driver.find_element(By.CLASS_NAME, 'mdc-button--raised')
#submitButton.click()

#print(email)
time.sleep(3)
driver.close()
