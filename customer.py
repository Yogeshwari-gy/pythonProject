from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://qa.chups.com/")
time.sleep(5)
driver.find_element(By.ID,"loc-input").send_keys("3244 west lincoln avenue")
time.sleep(10)
driver.find_element(By.XPATH,"//button[contains(text(),'Dine-In')]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//p[contains(text(),'Chennai Tiffins Social Kitchen')]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//h4[contains(text(),'Chennai Tiffins')]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//h3[contains(text(),'Idly')]").click()
time.sleep(4)
driver.find_element(By.XPATH,"//label[contains(text(),'water')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
time.sleep(2)
# driver.find_element(By.XPATH,"//h3[contains(text(),'Buffalo Wings')]").click()
# driver.find_element(By.XPATH,"label[contains(text(),'Blue Cheese')]").click()
# driver.find_element(By.XPATH,"//label[contains(text(),'12 Pcs')]").click()
#
# driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//p[contains(text(),'Add Special Instruction')]").click()
driver.find_element(By.XPATH,"//textarea[@placeholder='Type here eg: Need cilantro or No onions']").send_keys("Add extra sambar")
driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
time.sleep(6)
driver.find_element(By.XPATH,"//input[@id='yourname']").send_keys("Yamini")
driver.find_element(By.XPATH,"//input[@id='emailid']").send_keys("test@g.com")
driver.find_element(By.XPATH,"//input[@id='phoneno']").send_keys("3213213211")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='d-flex align-items-center justify-content-center']")
driver.find_element(By.XPATH,"//input[@class='mx-2 p-2']").send_keys("123")
driver.find_element(By.XPATH,"//button[contains(text(),'Verify & Proceed')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='unitnumber']").send_keys("Lab")
driver.find_element(By.XPATH,"//button[contains(text(),'Pick-Up')]").click()
time.sleep(4)
# driver.find_element(By.XPATH,"//span[contains(text(),'04:31 AM - 05:00 AM')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
time.sleep(20)
driver.find_element(By.XPATH,"//span[contains(text(),'Pay Later')]").click()
time.sleep(10)
