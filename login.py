from selenium import webdriver
from selenium.webdriver import Actions, Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#import time
driver = webdriver.Firefox()
driver.get("https://mygoldenqa.arlo.com/#/login")
loginForm = driver.find_element(By.ID,"loginForm")
driver.find_element(By.ID, "loginEmail").send_keys("arloqaregister+1701127729525jwrn+us@gmail.com")
driver.find_element(By.ID, "loginPassword").send_keys("Netgear1")
loginButton = driver.find_element(By.ID,"loginForm")
loginButton.submit()


#print(email)
#time.sleep(15)
#driver.close()