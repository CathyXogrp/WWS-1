# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.webdriver import FirefoxProfile

class WWSLogin(unittest.TestCase):
    def setUp(self):
        LocalProfile = "C:\Users\lewu\AppData\Roaming\Mozilla\Firefox\Profiles\gos1173o.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wws_login(self):
        driver = self.driver
        driver.get(self.base_url + "/gs/dashboard")
        firstwindow = driver.window_handles[0]
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        driver.switch_to_frame(driver.find_element_by_css_selector(".dialog-content"))
        #time.sleep(5)
        driver.find_element_by_css_selector(".join-container>.btn-alternate").click()
        #time.sleep(5)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("Calla4@gmail.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        driver.switch_to_window(firstwindow)

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
