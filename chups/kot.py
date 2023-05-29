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
driver.get("https://qa.skycooking.com/")
time.sleep(5)
a = driver.find_element(By.XPATH,"//*[@class='form-control mb-1 pac-target-input']")
print(a)
b = driver.find_element(By.XPATH,"//input").send_keys('91367')
print(b)

c = driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-lg w-100 text-uppercase fw-bold my-3']").click()
time.sleep(5)
d = driver.find_element(By.XPATH,
    "//button[@class='btn btn-primary btn-lg w-100 text-uppercase fw-bold my-3']").send_keys(Keys.ENTER)
time.sleep(2)
#driver.find_element(By.XPATH,"//span[contains(text(),'Enable Location Search')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Dine-In')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//h3[contains(text(),'Los Angeles')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//h4[contains(text(),'Deez  Wings')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//h3[contains(text(),'Garlic Parm Fries')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//h3[contains(text(),'Buffalo Wings')]").click()
driver.find_element(By.XPATH,"label[contains(text(),'2')]").click()
driver.find_element(By.XPATH,"//label[contains(text(),'12 Pcs')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Add Special Instruction')]").click()
driver.find_element(By.XPATH,"//textarea").send_keys("Add extra pepper")
driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='yourname']").send_keys("Yamini")
driver.find_element(By.XPATH,"//input[@id='phoneno']").send_keys("3213213211")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='d-flex align-items-center justify-content-center']")
driver.find_element(By.XPATH,"//input[@class='mx-2 p-2']").send_keys("123")
driver.find_element(By.XPATH,"//button[contains(text(),'Verify & Proceed')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'04:00 AM - 11:55 PM')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
