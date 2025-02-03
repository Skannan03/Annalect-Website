# Import all the necessary libraries
import time  # for time delay
import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class careerpage(Basepage):
    career = (By.XPATH, "//*[contains(text(),'Careers')]")
    title = (By.XPATH, "//a[@title='Annalect']")
    find_career = (By.XPATH, "//a[contains(text(),'Find Careers in the US')]")
    across_globe = (By.XPATH, "//a[contains(text(),'Across the Globe')]")
    def Career(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to  section
        self.hrm_btn_click(self.career)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "team" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Career page ")
            return True
        else:
            print("F- The automation is not directed to Our Team page")
            return False

    def Find_career(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.career)
        self.hrm_btn_click(self.find_career)

    def Across_globe(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.career)
        self.hrm_btn_click(self.across_globe)
