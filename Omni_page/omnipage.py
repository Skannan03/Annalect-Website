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


class omnipage(Basepage):
    meet_omni = (By.XPATH, "//*[contains(text(),'Meet Omni')]")
    download_btn = (By.CSS_SELECTOR, ".button.full-width.muted-omni-blue.pdf-button")
    see_how_omni_work = (By.CSS_SELECTOR, ".button.muted-omni-blue")
    title = (By.XPATH, "//a[@title='Annalect']")
    iframe= (By.XPATH, "//iframe[contains(@id, 'hs-form-iframe')]")
    email = (By.XPATH, "//input[@name='email']")
    fullname = (By.XPATH, "//input[@name='full_name']")
    jobtitle = (By.XPATH, "//input[@name='jobtitle']")
    company = (By.XPATH, "//input[@name='company']")
    # companysize = (By.XPATH, "//input[@name='company_size1']")
    location = (By.XPATH, "//input[@name='location']")
    function = (By.XPATH, "//input[@name='function']")
    checkbox = (By.XPATH, "//input[@id='LEGAL_CONSENT.subscription_type_130294659-c582604b-9a31-4263-afec-2f874ced1b27']")
    downloadbtn = (By.CSS_SELECTOR, "input[value='Download PDF']")

    def Download(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.meet_omni)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section
        time.sleep(3)
        self.hrm_btn_click(self.download_btn)

    def See_how_omni_works(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.meet_omni)
        self.driver.execute_script("window.scrollTo(0,3100);")  # Scroll to blog section
        self.hrm_btn_click(self.see_how_omni_work)

    def Download_Page(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.meet_omni)
        self.hrm_btn_click(self.download_btn)

    def Download1(self, email, name, job, company):
        self.driver.refresh()
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.meet_omni)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section
        self.hrm_btn_click(self.download_btn)
        self.driver.execute_script("window.scrollTo(0,200);")  # Scroll to blog section

        iframe_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@id, 'hs-form-iframe')]"))
        )
        self.driver.switch_to.frame(iframe_element)

        self.hrm_send_keys(self.email, email)
        self.hrm_send_keys(self.fullname, name)
        self.hrm_send_keys(self.jobtitle, job)
        self.hrm_send_keys(self.company, company)
        companysize = self.driver.find_element(By.XPATH, "//input[@name='company_size1']")
        x = Select(companysize)
        x.select_by_index(2)

        y = Select(self.driver.find_element(self.location))
        y.select_by_value("Canada")

        z = Select(self.driver.find_element(self.function))
        z.select_by_visible_text("Media Services")

        self.hrm_btn_click(self.checkbox)
        self.driver.switch_to.default_content()
        self.driver.refresh()

    def Download2(self, email, name, job, company):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.meet_omni)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section
        self.hrm_btn_click(self.see_how_omni_work)
        self.hrm_send_keys(self.email, email)
        self.hrm_send_keys(self.fullname, name)
        self.hrm_send_keys(self.jobtitle, job)
        self.hrm_send_keys(self.company, company)
        x = Select(self.driver.find_element(self.companysize))
        x.select_by_index(2)

        y = Select(self.driver.find_element(self.location))
        y.select_by_value("Canada")

        z = Select(self.driver.find_element(self.function))
        z.select_by_visible_text("Media Services")

        self.hrm_btn_click(self.checkbox)

