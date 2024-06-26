import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestClass(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div["
                                           "1]/div[1]/div[2]/input[1]").send_keys("Toronto")
        time.sleep(2)
        log.info("checking available rentalss")
        self.driver.find_element(By.XPATH, "//div[@class='data text-dark w-100 py-3 px-3']/i").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder=' Pickup Date']").click()
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
        select.select_by_value('11')
        time.sleep(2)
        select1 = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
        select1.select_by_value("2024")
        self.driver.execute_script("window.scrollBy(0,200)")
        time.sleep(2)
        parent = self.driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']")
        child_elements = parent.find_elements(By.XPATH, "//div[@class='react-datepicker__week']//div[@role='option']")

        for day in child_elements:
            if day.text == '15':
                day.click()
                break
        select1 = Select(self.driver.find_element(By.XPATH, "//select[@class='form-select px-1 PickupTime']"))
        select1.select_by_value('11:30')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dropoff Date']").click()
        time.sleep(2)
        select2 = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
        select2.select_by_value('11')
        select3 = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
        select3.select_by_value('2024')
        time.sleep(2)
        pelement = self.driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']")
        celement = pelement.find_elements(By.XPATH, "//div[@class='react-datepicker__week']//div[@role='option']")
        for dates in celement:
            if dates.text == '17':
                dates.click()
                break
        select4 = Select(self.driver.find_element(By.XPATH, "//select[@class='w-100 form-select px-1 PickupTime']"))
        select4.select_by_value('11:30')
        time.sleep(2)
        select5 = Select(self.driver.find_element(By.XPATH, "//select[@class='Residential form-select pt-0 ps-2']"))
        select5.select_by_value("Canada")
        self.driver.find_element(By.XPATH, "//button[@class=' Reserve_button btn btn-btn-lg']").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1300)")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-1300)")
        time.sleep(2)
        log.info("checking modify")
        self.driver.find_element(By.XPATH, "//button[text()='Modify Search']").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1300)")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-1300)")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Country,city, Airport Code']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Country,city, Airport Code']").send_keys("YYZ")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class='dropdownPicker'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='City ,Country, Airport Code']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='City ,Country, Airport Code']").send_keys("yyZ")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Find Car']").click()
        select = Select(self.driver.find_element(By.XPATH, "//select[@class='form-select w-100']"))
        select.select_by_visible_text("Select All")
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "(//select[@class='form-select'])[1]"))
        select.select_by_visible_text("Select All")
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "(//select[@class='form-select'])[2]"))
        select.select_by_visible_text("Select All")
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "(//select[@class='form-select'])[3]"))
        select.select_by_visible_text("Select All")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class='dots d-flex']/div)[2]").click()
        time.sleep(2)
        log.info("viewing cars")
        self.driver.find_element(By.XPATH, "(//div[@class='dots d-flex']/div)[1]").click()
        assert self.driver.find_element(By.XPATH, "//label[@class='text-center']").text == "Service Provided By"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='View Vehicle Information']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Close Vehicle Information']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='PAY NOW'][1]").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(2)
        element = self.driver.find_element(By.XPATH,
                                           "//div[@class='row']//button[@type='button'][normalize-space()='Proceed to "
                                           "checkout']")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        log.info(self.driver.find_element(By.XPATH, "(//div[@id='container-row'])[1]").text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Test")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Tester")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']").send_keys("7676859969")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("test@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Confirm Email Address']").send_keys("test@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']").click()
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
        select.select_by_value('7')
        time.sleep(2)
        dropdown_element = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollTop -= 100;", dropdown_element)
        time.sleep(2)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value('1997')
        time.sleep(2)
        month = self.driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']")
        week = month.find_elements(By.XPATH, "//div[@class='react-datepicker__week']//div[@role='option']")
        for dates in week:
            if dates.text == '2':
                dates.click()
                break
        self.driver.find_element(By.XPATH, "//input[@id = 'inputAddress']").send_keys("address")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class=' css-19bb58m'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='India']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class=' css-hlgwow'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='Karnataka']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class=' css-b62m3t-container'])[3]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='Bengaluru']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='ZIP Code']").send_keys("54768")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Flight Details/Number']").send_keys("12345")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Name On Card']").send_keys("Test Tester")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400)")
        self.driver.find_element(By.XPATH, "//input[@id='ccn']").send_keys("4242424242424242")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Expiry Date']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Dec']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter CVC']").send_keys("123")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,200)")
        time.sleep(2)



        # self.driver.find_element(By.XPATH, "//button[@class='btn-close']").click()
