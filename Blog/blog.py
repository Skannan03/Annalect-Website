# Import all the necessary libraries
import time  # for time delay
from selenium.webdriver.common.action_chains import ActionChains

import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.ui import Select  # Used to select the dropdown
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class blogpage(Basepage):
    title = (By.XPATH, "//a[@title='Annalect']")
    blog = (By.XPATH, "//li[@id='menu-item-15536']")
    categories = (By.XPATH, "//ul[@class='category-filter clearfix posts-filter']/li")
    blog_img = (By.XPATH, "(//div[@class='item-image post-media'])")
    blog_category = (By.CSS_SELECTOR, ".post-meta-categories")
    blog_headline = (By.CSS_SELECTOR, ".page-title.entry-title")
    blog_title = (By.XPATH, "(//h2[@class='post-title entry-title'])")
    read_more = (By.XPATH, "(//a[@class='more-link'])")

    def Blog(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.blog)
        category_element = self.hrm_visibility_elements(self.categories)

        for i in category_element:
            category_text = i.text
            print(f"Clicking on category: {category_text}")
            i.click()
            time.sleep(2)


    def Blog_navigate_and_verify(self, element_locator):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.blog)
        category_element = len(self.hrm_visibility_elements(self.categories))

        for i in range(category_element):
            categories = self.hrm_visibility_elements(self.categories)
            category = categories[i]
            category_text = category.text
            print(f"Clicking on category: {category_text}")
            category.click()
            time.sleep(2)
            self.hrm_btn_click(element_locator)
            b_headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
            print(f"The Headline of the blog :={b_headline}")
            b_category = self.hrm_get_text_element(self.blog_category)  # Get category
            print(f"The blog is from category:={b_category}")
            return bool(b_headline) and bool(b_category)

            self.hrm_btn_click(self.blog)
            time.sleep(2)
