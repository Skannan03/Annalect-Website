# Import all the necessary libraries
import time  # for time delay
import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class leadership_page(Basepage):
    leadership = (By.XPATH, "//*[contains(text(),'Leadership')]")
    title = (By.XPATH, "//a[@title='Annalect']")
    page_title1 = (By.CSS_SELECTOR, ".page-title.entry-title")
    leader_title1 = (By.XPATH, "(//div[@class='vc_pageable-slide-wrapper vc_clearfix'])[1]/div")
    page_title2 = (By.XPATH, "//div[@class='wpb_wrapper']/h2")
    leader_title2 = (By.XPATH, "(//div[@class='vc_pageable-slide-wrapper vc_clearfix'])[2]/div")
    leader_page_name = (By.CSS_SELECTOR, '.page-title.entry-title')
    leader_page_position = (By.CSS_SELECTOR, '.professional-title')
    leaders_img = (By.XPATH, "//div[@class='vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn']")
    leaders_name = (By.XPATH, "//div[@class='vc_col-sm-12 vc_gitem-col vc_gitem-col-align-']/div/h3/a")
    leader_position = (By.CSS_SELECTOR, "vc_gitem-acf.vc_gitem-align-center.field_547de98a19f22")
    scrollup = (By.XPATH, "//a[@id='to-top']")

    def Leadership(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.leadership)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "leadership" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Leadership page ")
            return True
        else:
            print("F- The automation is not directed to Leadership page")
            return False

    def Page_Headers(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.leadership)
        title = self.hrm_get_text_element(self.page_title1)
        print(f"The Page Title is {title}")
        leader_ele1 = self.hrm_visibility_elements(self.leader_title1)
        print(f"Found {len(leader_ele1)} leaders.")
        title = self.hrm_get_text_element(self.page_title2)
        print(f"The Page Title is {title}")
        leader_ele2 = self.hrm_visibility_elements(self.leader_title2)
        print(f"Found {len(leader_ele2)} leaders.")

    def Leadersimg(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.leadership)
        leader_elements = self.hrm_visibility_elements(self.leaders_img)
        for i in leader_elements:
            i.click()
            self.driver.execute_script("window.scrollTo(0,400);")  # Scroll to section
            name = self.hrm_get_text_element(self.leader_page_name)
            print(f"The Name of the Leader is {name}")
            position = self.hrm_get_text_element(self.leader_page_position)
            print(f"The Name of the Leader is {position}")
            print("--------------------------------------------------------------")
            self.driver.back()

    def Leaders_name(self):
        self.driver.execute_script("window.scrollTo(0, 0)")  # Navigate to top
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.leadership)
        self.driver.execute_script("window.scrollTo(0,200);")
        leader_elements = self.hrm_visibility_elements(self.leaders_name)
        for i in leader_elements:
            i.click()
            self.driver.execute_script("window.scrollTo(0,400);")  # Scroll to section
            name = self.hrm_get_text_element(self.leader_page_name)
            print(f"The Name of the Leader is {name}")
            position = self.hrm_get_text_element(self.leader_page_position)
            print(f"The Name of the Leader is {position}")
            print("--------------------------------------------------------------")
            self.driver.back()

    def Scrollup(self):
        time.sleep(5)
        self.hrm_btn_click(self.scrollup)  # Scrolling to Top of the page
        time.sleep(4)
