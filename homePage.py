from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://mygoldenqa.arlo.com/#/home")
signIn = driver.find_element(By.CLASS_NAME,'basic-link')
#driver.find_element(By.ID, "loginEmail").send_keys("arloqaregister+1701127729525jwrn+us@gmail.com")
#driver.find_element(By.ID, "loginPassword").send_keys("Netgear1")
#signInButton = driver.find_element(By.CLASS_NAME,"login-button-home")
signIn.click()


#print(email)
time.sleep(5)
driver.close()
