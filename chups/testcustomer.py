from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
@pytest.fixture()
def test_customer():
    global driver
    serv_obj=Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://qa.chups.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID,"loc-input").send_keys("23830 , Califa Street, Los Angeles, California 91367")
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[contains(text(),'Dine-In')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//p[contains(text(),'Chennai Tiffins Social Kitchen')]").click()
    time.sleep(10)
@pytest.mark.skip()
def test_search(test_customer):
    driver.find_element(By.ID,"searchbar").send_keys("biriyani")
    driver.find_element(By.ID,"searchbar").send_keys(Keys.ENTER)
    time.sleep(20)
    driver.find_element(By.XPATH,"//h3[contains(text(),'Biryani Rice Combo Box 4')]").click()
    time.sleep(15)
    driver.find_element(By.XPATH,"//label[contains(text(),'Coke (250 ml)')]").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='yourname']").send_keys("Yamini")
    driver.find_element(By.XPATH, "//input[@id='emailid']").send_keys("test@g.com")
    driver.find_element(By.XPATH, "//input[@id='phoneno']").send_keys("3213213211")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='d-flex align-items-center justify-content-center']")
    driver.find_element(By.XPATH, "//input[@class='mx-2 p-2']").send_keys("123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Verify & Proceed')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='unitnumber']").send_keys("Lab")
    # driver.find_element(By.XPATH, "//button[contains(text(),'Pick-Up')]").click()
    # time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"//span[contains(text(),'Pay Later')]").click()
    time.sleep(10)
@pytest.mark.skip()
def test_diffitems_diffbrands(test_customer):
    driver.find_element(By.XPATH,"//h4[contains(text(),'Biriyani Factory')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//span[contains(text(),'Browse Menu')]").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//div[contains(text(),'Biriyani')]").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//h3[contains(text(),'Prawn Biryani')]").click()
    driver.find_element(By.XPATH,
                        "//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//img[@alt='Chups']").click()
    time.sleep(25)
    # # driver.find_element(By.XPATH,"//h4[contains(text(),'Willie's BBQ & Smoke House')]").click()
    driver.find_element(By.XPATH,"//h4[contains(text(),'Chennai Tiffins(Anjappar)')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//h3[contains(text(),'Idly')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//label[contains(text(),'water')]").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
    time.sleep(2)
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
    # driver.find_element(By.XPATH,"//button[contains(text(),'Pick-Up')]").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH,"//img[@alt='Coupon']").click()
    # # driver.find_element(By.XPATH,"//span[contains(text(),'04:31 AM - 05:00 AM')]").click()
    # driver.find_element(By.XPATH,"//div[contains(text(),'Apply Rewards / Coupons')]").click()
    # time.sleep(4)
    # driver.find_element(By.XPATH,"//p[contains(text(),'Apply')]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
    time.sleep(20)
    # driver.find_element(By.XPATH,"//span[contains(text(),'Add Credit Card')]").click()
    # time.sleep(10)
    # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "card-data-wrapper")))
    # # WebDriverWait(driver, 20).until(
    # #     EC.element_to_be_clickable((By.XPATH, "//div[@data-card-field-placeholder='Card number']"))).send_keys("1234")
    # # driver.find_element(By.XPATH, "//input[@placeholder='Card number']").click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable
    #                                 ((By.XPATH, "//input[@placeholder='Card number']"))).send_keys("4111111111111111")
    # # driver.find_element(By.ID,"form")
    # # driver.find_element(By.XPATH,"//div[@class='sq-input-wrapper card-input-wrapper']").click()
    # driver.find_element(By.XPATH,"//input[@placeholder='Card number']").click()
    # driver.find_element(By.XPATH,"//input[@placeholder='Card number']").send_keys("4111111111111111")
    # # driver.find_element(By.ID,"card-data-wrapper").click()
    # driver.find_element(By.XPATH,"//input[@placeholder='MM/YY']").send_keys("01/25")
    # driver.find_element(By.XPATH,"//input[@placeholder='CVV']").send_keys("123")
    # driver.find_element(By.ID,"postalCode").send_keys("21346")
    driver.find_element(By.XPATH,"//span[contains(text(),'Pay Later')]").click()
    time.sleep(10)
@pytest.mark.skip()
def test_changekitchen(test_customer):
    # driver.find_element(By.XPATH,"//span[contains(text(),'expand_more')]").click()
    driver.find_element(By.XPATH,"//span[@class='location_name']").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"//h3[contains(text(),'Disneyland Park')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//h4[contains(text(),'Briyani Factory')]").click()
    time.sleep(15)
    # driver.find_element(By.XPATH, "//h3[contains(text(),'Tamil Style veg biriyani')]").click()
    # driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
    # time.sleep(2)
    # driver.find_element(By.ID,"btn-delivery").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//h3[contains(text(),'Warner Center Park')]").click()
    # time.sleep(10)
    # driver.find_element(By.XPATH,"//button[contains(text(),'Go Back')]").click()
    # driver.find_element(By.ID, "btn-delivery").click()
    # driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]").click()
    # time.sleep(25)
    driver.find_element(By.XPATH,"//input[@type='search']").click()
    time.sleep(5)
    driver.find_element(By.ID, "searchbar").send_keys("coke")
    time.sleep(15)
    driver.find_element(By.XPATH, "//h3[contains(text(),'Coke')]").click()
    driver.find_element(By.XPATH,
                        "//button[@class='btn btn-primary btn-default btn-lg text-uppercase d-flex align-items-center justify-content-between w-100']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='yourname']").send_keys("Yamini")
    driver.find_element(By.XPATH, "//input[@id='emailid']").send_keys("test@g.com")
    driver.find_element(By.XPATH, "//input[@id='phoneno']").send_keys("3213213211")
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='d-flex align-items-center justify-content-center']")
    driver.find_element(By.XPATH, "//input[@class='mx-2 p-2']").send_keys("123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Verify & Proceed')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
    time.sleep(20)
    driver.find_element(By.XPATH, "//span[contains(text(),'Pay Later')]").click()
    time.sleep(10)
    # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"card-data-wrapper")))
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[@data-card-field-placeholder='Card number']"))).send_keys("1234")
    # driver.find_element(By.XPATH, "//input[@placeholder='Card number']").click()
    # driver.find_element(By.XPATH,"//input[@placeholder='Card number']").send_keys("4111111111111111")
@pytest.mark.skip()
def test_menu(test_customer):
    # driver.find_element(By.XPATH,"//li[contains(text(),'About US')]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH,"//li[contains(text(),'Contact Us')]").click()
    # time.sleep(4)
    # driver.find_element(By.ID,"yourname").send_keys("Yamini")
    # driver.find_element(By.ID,"phoneno").send_keys("0020200202")
    # driver.find_element(By.ID,"Subject").send_keys("Enquiry")
    # driver.find_element(By.ID,"Message").send_keys("Ease of use but got to choose different brands")
    # # driver.find_element(By.XPATH,"//button[contains(text(),'Send')]").click()
    driver.find_element(By.XPATH,"//li[contains(text(),'Private Events')]").click()
    time.sleep(4)
    driver.find_element(By.ID, "yourname").send_keys("Yamini")
    driver.find_element(By.ID, "phoneno").send_keys("0020200202")
    driver.find_element(By.ID,"email_address").send_keys("yogi@gmail.com")
    driver.find_element(By.ID,"typeofevent").send_keys("Birthday Party")
    driver.find_element(By.XPATH,"//input[@placeholder='MM/DD/YYYY']").click()
    driver.find_element(By.XPATH,"//div[contains(text(),'15')]").click()
    driver.find_element(By.ID,"guest").send_keys(20)
    driver.find_element(By.XPATH,"//div[contains(text(),'Select')]").click()