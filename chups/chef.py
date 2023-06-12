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
def test_chef():
    global driver
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://qa2.chups.com/")
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("harry@yahoo.com")
    driver.find_element(By.ID, "exampleFormControlInput2").send_keys("welcome")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(15)
    yield
    print("Test Completed")
@pytest.mark.skip()
def test_cal(test_chef):
    driver.find_element(By.CSS_SELECTOR, '#calimg').click()
    driver.find_element(By.XPATH, "//abbr[@aria-label='June 9, 2023']").click()
    driver.find_element(By.XPATH, "//div[contains(@class, 'sidebar') and contains(@class, 'fixed-top')]/preceding-sibling::div[contains(@class, 'd-flex') and contains(@class, 'align-items-center')]/IMG[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(text(),'KOT')]").click()
    for i in range(6):
        driver.find_element(By.XPATH, "//DIV[@id='left-tabs-example-tabpane-first']/DIV[1]/DIV[1]/DIV[1]/H2[1]/BUTTON[1]/DIV[1]/DIV[6]/DIV[1]/BUTTON[1]").click()
        # driver.find_element(By.XPATH, "//button[contains(text(),'Waiting')]").click()
        time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(text(),' Waiting')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(text(),' Preparing')]").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//a[contains(text(),' Completed')]").click()
    time.sleep(4)
@pytest.mark.skip()
def test_logout(test_chef):
    driver.find_element(By.XPATH, "//div[contains(@class, 'sidebar') and contains(@class, 'fixed-top')]/preceding-sibling::div[contains(@class, 'd-flex') and contains(@class, 'align-items-center')]/IMG[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(text(),'Log Out')]").click()
    time.sleep(5)
def test_hamburger(test_chef):
    driver.find_element(By.XPATH, "//div[contains(@class, 'sidebar') and contains(@class, 'fixed-top')]/preceding-sibling::div[contains(@class, 'd-flex') and contains(@class, 'align-items-center')]/IMG[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(text(),'Tutorials')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[contains(text(),'Falooda Milk Tea')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys("biriyani")
    driver.find_element(By.XPATH, "//span[contains(text(),'Nizam Boneless Chicken Biriyani')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//img[@alt='back']").click()
    driver.find_element(By.XPATH,
                        "//div[contains(@class, 'sidebar') and contains(@class, 'fixed-top')]/preceding-sibling::div[contains(@class, 'd-flex') and contains(@class, 'align-items-center')]/IMG[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(text(),'Setting')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]").click()
    time.sleep(5)


