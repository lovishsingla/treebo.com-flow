#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Treeboflow(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/lovish/Downloads/geckodriver')
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def testTitle(self):
        self.driver.get('https://www.treebo.com/')
        self.assertIn('Treebo', self.driver.title)
        
        
        elem = self.driver.find_element_by_link_text("Login")
        elem.click()
        self.driver.implicitly_wait(1)

        elem = self.driver.find_element_by_name("email") 
        elem.send_keys("rlovish007@gmail.com")
        elem = self.driver.find_element_by_name("password") 
        elem.send_keys("qwerty1234")
        elem = self.driver.find_element_by_name("button")
        elem.click()
        self.driver.implicitly_wait(10)

        elem = self.driver.find_element_by_xpath("//div[@class='navbar__link navbar__login']")
        elem.click()
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element_by_xpath("//a[@href='/account/profile']")
        elem.click()
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_id("firstName")
        elem.clear() 
        elem.send_keys("Lovish")     
        elem = self.driver.find_element_by_id("lastName")
        elem.clear() 
        elem.send_keys("Singla")
        elem = self.driver.find_element_by_id("location")
        elem.clear()
        elem.send_keys("Bengluru")
        elem = self.driver.find_element_by_id("submitProfileDetail")
        elem.click()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)