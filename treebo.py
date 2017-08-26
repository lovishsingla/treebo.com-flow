#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Treeboflow(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/lovish/Downloads/geckodriver')
        
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

        elem = self.driver.find_element_by_class_name("react-autosuggest__input")
        elem.send_keys("Bengluru")
        elem = self.driver.find_element_by_xpath(".//*[@id='react-autowhatever-1--item-0']")
        elem.click()
        elem = self.driver.find_element_by_id("startDate")
        elem.click()
        elem = self.driver.find_element_by_xpath(".//*[@id='wrapper']/div[2]/section[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr[3]/td[3]")
        elem.click()
        elem = self.driver.find_element_by_xpath(".//*[@id='wrapper']/div[2]/section[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr[3]/td[6]")
        elem.click()
        elem = self.driver.find_element_by_class_name("occupancy__header")
        elem.click()
        elem = self.driver.find_element_by_xpath("//div[@class='occupancy__options occupancy__options--show']/div[1]")
        elem.click()
        self.driver.implicitly_wait(3)
        elem = self.driver.find_element_by_xpath("//button[@class='button button--block search-button__cta']")
        elem.click()
        
        self.driver.implicitly_wait(7)
        elem = self.driver.find_element_by_xpath("//i[@class='rp-aside__toggle-icon icon-plus']")
        elem.click()
        
        self.driver.implicitly_wait(2)
        elem = self.driver.find_element_by_xpath("//div[@class='text-2 rp-sort__item rp-sort__item--selected']")
        elem.click()
        
        self.driver.implicitly_wait(2)
        
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "priceRanges-0"))
        )
        elem.click()
        
        elem = self.driver.find_element_by_xpath("//a[@class='button r-hotel__action']")
        elem.click()
        self.driver.implicitly_wait(5)
        
        elem = self.driver.find_element_by_id("name")
        elem.send_keys("Lovish")
        elem = self.driver.find_element_by_id("mobile")
        elem.send_keys("9591028847")
        elem = self.driver.find_element_by_name("button")
        elem.click()
        self.driver.implicitly_wait(5)
        
        elem = self.driver.find_element_by_name("message")
        elem.send_keys("abcd")
        time.sleep(5)
        elem = self.driver.find_element_by_xpath("//button[@class='checkout__action button checkout__action--secondary button--secondary']")
        elem.click()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)