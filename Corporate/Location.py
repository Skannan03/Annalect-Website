# Import all the necessary libraries
import time  # for time delay
import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class location_page(Basepage):
    title = (By.XPATH, "//a[@title='Annalect']")
    location = (By.XPATH, "//*[contains(text(),'Locations')]")
    page_title = (By.CSS_SELECTOR, ".page-title.entry-title")
    countries_header = (By.XPATH, "//ul[@data-vc-grid-filter='category']/li")
    country_loc = (By.XPATH, "//div[@class='vc_col-sm-12 vc_gitem-col vc_gitem-col-align-']")
    location_name = (By.XPATH, "//a[@class='vc_gitem-link']")
    location_address = (By.XPATH, "//div[@class='vc_gitem-acf field_58a23764c8991']")
    location_tele = (By.XPATH, "//div[@class='vc_gitem-acf location-phone-field field_5fcf87f998e78']")

    def Location(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.location)
        header = self.hrm_get_text_element(self.page_title)
        print(f"The Page Title is {header}")
        country_ele = self.hrm_visibility_elements(self.countries_header)
        print(f"Found {len(country_ele)} country headers.")

        print("The Names of the header locations are:")
        for index, element in enumerate(country_ele, start=1):
            print(f"{index}: {element.text.strip()}")

    def Total_location(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.location)
        location_ele = self.hrm_visibility_elements(self.country_loc)
        print(f"Found {len(location_ele)} location in world wide.")
        print("The Names of the header locations are:")
        for index, element in enumerate(location_ele, start=1):
            print(f"{index}: {element.text.strip()}")








