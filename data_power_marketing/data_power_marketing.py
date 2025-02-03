# Import all the necessary libraries
import time  # for time delay
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class data_power_market_page(Basepage):
    learn_more = (By.XPATH, "(//a[@class='button arrow-down'])[1]")
    data_power_market = (By.XPATH, "//li[@id='menu-item-14636']")
    title = (By.XPATH, "//a[@title='Annalect']")
    omni_glance = (By.XPATH, "//a[@class='button full-width pdf-button']")
    vertical_ss = (By.XPATH, "//a[@class='button full-width']")
    iframe = (By.XPATH, "//iframe[contains(@id, 'hs-form-iframe')]")
    email = (By.XPATH, "//input[@name='email']")
    fullname = (By.XPATH, "//input[@name='full_name']")
    jobtitle = (By.XPATH, "//input[@name='jobtitle']")
    company = (By.XPATH, "//input[@name='company']")
    companysize = (By.ID, "company_size1-212d8a14-83ea-43a6-89fb-9ffa956c360e")
    location = (By.ID, "location-212d8a14-83ea-43a6-89fb-9ffa956c360e")
    function = (By.ID, "function-212d8a14-83ea-43a6-89fb-9ffa956c360e")
    checkbox = (By.NAME, "LEGAL_CONSENT.subscription_type_130294659")
    downloadbtn = (By.CSS_SELECTOR, "input[value='Download PDF']")


    vertical = (By.XPATH, "(//select[@id='vertical-553bc5f9-7c95-4793-a4e8-c666621a58c1'])")
    companysize_v= (By.ID, "company_size1-553bc5f9-7c95-4793-a4e8-c666621a58c1")
    location_v = (By.ID, "location-553bc5f9-7c95-4793-a4e8-c666621a58c1")
    function_v = (By.ID, "function-553bc5f9-7c95-4793-a4e8-c666621a58c1")

    def Learn_more(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.data_power_market)
        self.hrm_btn_click(self.learn_more)

    def Omni_glance(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.data_power_market)
        self.driver.execute_script("window.scrollTo(0,3100);")
        self.hrm_btn_click(self.omni_glance)

    def Vertical_ss(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.data_power_market)
        self.driver.execute_script("window.scrollTo(0,3100);")
        self.hrm_btn_click(self.vertical_ss)

    def Download_details(self, email, name, job, company):
        self.driver.refresh()
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.data_power_market)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section
        self.hrm_btn_click(self.omni_glance)
        self.driver.execute_script("window.scrollTo(0,200);")  # Scroll to blog section

        iframe_element = self.hrm_visibility_element(self.iframe)
        self.driver.switch_to.frame(iframe_element)
        self.hrm_send_keys(self.email, email)
        self.hrm_send_keys(self.fullname, name)
        self.hrm_send_keys(self.jobtitle, job)
        self.hrm_send_keys(self.company, company)
        x = Select(self.driver.find_element(*self.companysize))
        x.select_by_index(2)

        y = Select(self.driver.find_element(*self.location))
        y.select_by_value("Canada")

        z = Select(self.driver.find_element(*self.function))
        z.select_by_visible_text("Media Services")

        self.hrm_btn_click(self.checkbox)
        self.driver.switch_to.default_content()

    def Vertical_details(self, email, name, job, company):
        self.driver.refresh()
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.data_power_market)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section
        self.hrm_btn_click(self.vertical_ss)
        self.driver.execute_script("window.scrollTo(0,200);")  # Scroll to blog section

        iframe_element = self.hrm_visibility_element(self.iframe)
        self.driver.switch_to.frame(iframe_element)
        self.hrm_send_keys(self.email, email)
        self.hrm_send_keys(self.fullname, name)
        self.hrm_send_keys(self.jobtitle, job)
        self.hrm_send_keys(self.company, company)

        w = Select(self.driver.find_element(*self.companysize_v))
        w.select_by_index(2)

        x = Select(self.driver.find_element(*self.location_v))
        x.select_by_value("Canada")

        y = Select(self.driver.find_element(*self.function_v))
        y.select_by_visible_text("Media Services")

        z = Select(self.driver.find_element(*self.vertical))
        z.select_by_index(2)

        self.hrm_btn_click(self.checkbox)
        self.driver.switch_to.default_content()
