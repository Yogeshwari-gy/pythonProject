from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pytest
@pytest.fixture()
def test_packer():
    global driver
    serv_obj=Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://qa2.chups.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("packhari@gmail.com")
    driver.find_element(By.ID, "exampleFormControlInput2").send_keys("welcome123")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(10)
def test_pack(test_packer):
    driver.find_element(By.CSS_SELECTOR,"#calimg").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//abbr[@aria-label='June 9, 2023']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(@class, 'sidebar') and contains(@class, 'fixed-top')]/preceding-sibling::div[contains(@class, 'd-flex') and contains(@class, 'align-items-center')]/IMG[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(text(),'KOT')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//DIV[@id='left-tabs-example-tabpane-first']/DIV[3]/DIV[1]/H2[1]/BUTTON[1]/DIV[1]/DIV[8]/H5[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[contains(@class, 'container-fluaid') and contains(@class, 'new-item-attribute')]/DIV[1]/DIV[1]/H2[1]/BUTTON[1]/DIV[1]/DIV[6]/DIV[1]/BUTTON[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'In-Progress')]").click()
    time.sleep(4)
    # driver.find_element(By.XPATH, "//button[contains(text(),'Start Packing')]").click()
    # driver.find_element(By.XPATH, "//button[contains(text(),'In-Progress')]").click()
    # time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(@class, 'cursor-pointer')]/IMG[1]").click()
    time.sleep(4)

    driver.close()
def testrunner(test_packer):
    driver.find_element(By.XPATH, "//BUTTON[@id='dropdown-autoclose-inside']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(@class, 'dropdown-menu') and contains(@class, 'show')]/A[2]").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,"#calimg").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//abbr[@aria-label='June 8, 2023']").click()
    time.sleep(2)
    for i in range(2):
        driver.find_element(By.XPATH, "//div[contains(@class, 'container-fluaid')]/DIV[1]/DIV[1]/H2[1]/BUTTON[1]/DIV[1]/DIV[10]/DIV[1]/BUTTON[1]").click()
        time.sleep(10)






