# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WwsAddEvent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wws_add_event(self):
        driver = self.driver
        driver.get(self.base_url + "/gs/dashboard")
        firstwindow = driver.window_handles[0]
        driver.find_element_by_css_selector(".landing-header-title-container>a:nth-of-type(1)").click() 
        #Click the Login link
        driver.switch_to_frame(driver.find_element_by_css_selector(".dialog-content"))
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("Calla4@gmail.com") # Enter the user name
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa") # Enter the password
        driver.find_element_by_name("button").click() #Click on Login button
        driver.switch_to_window(firstwindow)
        time.sleep(5)
        driver.find_element_by_css_selector(".travel>p:nth-of-type(1)").click()
        #time.sleep(5)
        driver.find_element_by_css_selector(".gallery-add-title").click()
        driver.find_element_by_id("item-name").click()
        driver.find_element_by_id("item-name").clear()
        driver.find_element_by_id("item-name").send_keys("test")
        driver.find_element_by_xpath("//div[@id='add-lc-dialog']/div/div/div[2]/label[3]").click()
        driver.find_element_by_name("location").click()
        driver.find_element_by_name("location").clear()
        driver.find_element_by_name("location").send_keys("hwrq")
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("464567787")
        driver.find_element_by_id("item-website").click()
        driver.find_element_by_id("item-website").clear()
        driver.find_element_by_id("item-website").send_keys("www.wtwtqwtqe.com")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("asdar@atawere.com")
        driver.find_element_by_xpath("//div[@id='add-lc-dialog']/div/div/div[2]/div[2]").click()
        driver.find_element_by_id("redactor-toolbar-0").click()
        driver.find_element_by_id("save-lc-item").click()
        time.sleep(5)
        driver.find_element_by_css_selector(".js-delete").click()
        driver.find_element_by_id("delete-item").click()
        #driver.find_elements_by_link_text("Wedding Website").click()
        #driver.find_element_by_css_selector(".accommodations>p:nth-of-type(1)").click() #click the add Accommodations link
        #driver.find_element_by_css_selector(".add-icon:nth-of-type(2)").click()
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else: 
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
