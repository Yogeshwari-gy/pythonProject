from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import pytest
@pytest.fixture()
def test_TestEs():
    global driver
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    #driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    driver.get("https://qa.chups.com/kiosk/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.NAME, "name").send_keys("whkiosk1@chups.com")
    driver.find_element(By.ID, "exampleFormControlInput2").send_keys("welcome")
    driver.find_element(By.XPATH, "//span[contains(text(),'show')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(4)
    yield
    print("Test completed")

# def test_Login(test_TestEs):
#     driver.find_element(By.NAME, "name").send_keys("whkiosk1@chups.com")
#     driver.find_element(By.ID, "exampleFormControlInput2").send_keys("welcome")
#     driver.find_element(By.XPATH, "//span[contains(text(),'show')]").click()
#     driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
#     time.sleep(4)
#     driver.close()
@pytest.mark.skip()
def test_ItemList(test_TestEs):
    driver.find_element(By.XPATH, "//h4[contains(text(),'A2B')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Veg rice')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'-')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='placebutton']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@class='mr-2 mb-1']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'×')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//label[contains(text(),'Name')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("yamini")
    time.sleep(2)
    driver.find_element(By.NAME, "mobileNumber").send_keys("9876543211")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Make Payment')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='form-group position-relative mb-4']")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@inputmode='numeric']").send_keys("123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Verify & Proceed')]").click()
    time.sleep(10)
    driver.close()
@pytest.mark.skip()
def test_ItemList2(test_TestEs):
    driver.find_element(By.XPATH, "//h4[contains(text(),'A2B')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Veg rice')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'-')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='placebutton']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@id='left-tabs-example-tab-second']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//img[@class='mr-2 mb-1']").click()
    # driver.find_element(By.XPATH,"//button[contains(text(),'Continue']").click()
    # time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Leave Checkout')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='searchText']").send_keys("Falooda")
    driver.find_element(By.XPATH,"//p[contains(text(),'Falooda Milk Tea')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH,"//h4[contains(text(),'Falooda Milk Tea')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//label[contains(text(),'Large')]").click()
    driver.find_element(By.XPATH,"//label[contains(text(),'Honey Boba')]").click()
    driver.find_element(By.XPATH,"//input[@name='specialInstrucion']").send_keys("Add more ice cubes")
    driver.find_element(By.XPATH,"//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@id='placebutton']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Name')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("yamini")
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),' No, I want to wait here for food')]").click()
    driver.find_element(By.XPATH, "//img[@src='/kiosk/static/images/remove-cart.svg']").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Make Payment')]").click()
    time.sleep(10)
    driver.close()

def test_Itemlist3(test_TestEs):
    driver.find_element(By.XPATH, "//h4[contains(text(),'A2B')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Veg rice')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'-')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='placebutton']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@class='r-home-menu']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//h4[contains(text(),'Biriyani Factory')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Dindigul Thalappakatti Biriyani')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='specialInstrucion']").send_keys("Add more spicy")
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.ID, "placebutton").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Name')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("yamini")
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),' No, I want to wait here for food')]").click()
    driver.find_element(By.XPATH, "//img[@src='/kiosk/static/images/remove-cart.svg']").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Make Payment')]").click()
    time.sleep(10)
    driver.close()
@pytest.mark.skip()
def test_Coupon(test_TestEs):
    driver.find_element(By.XPATH, "//h4[contains(text(),'A2B')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Veg rice')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'-')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='placebutton']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Name')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("yamini")
    driver.find_element(By.NAME, "mobileNumber").send_keys("9876543211")
    driver.find_element(By.XPATH,"//button[contains(text(),'View Coupon')]").click()
    time.sleep(3)
    # driver.find_element(By.NAME, "modalCouponCode").click()
    driver.find_element(By.NAME,"modalCouponCode").send_keys("CHUPS456")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[contains(text(),'Apply')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//span[contains(text(),'×')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Make Payment')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='form-group position-relative mb-4']")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@inputmode='numeric']").send_keys("123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Verify & Proceed')]").click()
    time.sleep(10)
    driver.close()
@pytest.mark.skip()
def test_Logout(test_TestEs):
    driver.find_element(By.XPATH, "//h4[contains(text(),'HOT BOX')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='jsx-3313785644 menu-details']")
    driver.find_element(By.XPATH, "//h4[contains(text(),'Chesse Sandwich')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'ADD TO CART - $')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='placebutton']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='left-tabs-example-tab-first']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@class='r-home-menu']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//img[@title='Logout']").click()
    time.sleep(2)
    driver.find_element(By.ID, "exampleFormControlInput1").send_keys("welcome")
    driver.find_element(By.XPATH, "//span[contains(text(),' Show ')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),' Hide ')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
    driver.close()
#
# def __init__main():
#     list=['Yamini','Yogi']
#     for i in list:
#         print("list")



