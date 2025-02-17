import mdc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import Actions, Keys

from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("https://mygoldenqa.arlo.com/#/login")
fp = driver.find_element(By.CLASS_NAME,'forget-password-link')
fp.click()
inputEmail = driver.find_element(By.ID, "email")
inputEmail.send_keys('arloqaregister+1731545247433azuy+us@gmail.com')
inputEmail.submit()
time.sleep(3)
reSend = driver.find_element(By.CLASS_NAME,'submit-button')
num = 1
while num <= 5:
    reSend.click()
    num = num + 1
    time.sleep(3)
    print(num)

time.sleep(10)
driver.close()