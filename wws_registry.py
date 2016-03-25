# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re
import random

class WwsRegistry(unittest.TestCase):
    def setUp(self):
        LocalProfile = "C:\Users\lewu\AppData\Roaming\Mozilla\Firefox\Profiles\gos1173o.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wws_registry(self):
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
        driver.find_element_by_link_text("Registry").click()
        driver.find_element_by_css_selector(".j-add-registry").click()
        driver.find_element_by_xpath(".//*[@id='create-registry']/ul/li[8]/div/a/img").click() 
        #Click on the Belk tab
        driver.find_element_by_xpath(".//*[@id='modal']/div/div/div/div[2]/div/div/a[1]").click()
        #Click on Create Registry link on the popup window
        #secondwindow = driver.window_handles[1]
        #driver.switch_to_window(secondwindow)
        #driver.find_element_by_link_text("get started").click()
        driver.get("https://www.belk.com/bridalregistry/create_signin.jsp")
        a = "".join(random.sample("qwertyuioplkjhgfdsazxcvbnm1234567890",5)) + "@mailinator.com"
        driver.find_element_by_id("txt_email_address_r").send_keys(a)
        driver.find_element_by_id("txt_email_address_ce").send_keys(a)
        driver.find_element_by_id("txt_password_r").send_keys("12345678")
        driver.find_element_by_id("txt_password_cp").send_keys("12345678")
        driver.find_element_by_css_selector(".orangeButtonSignInCA").click()
        
       

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
    
    #def tearDown(self):
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
