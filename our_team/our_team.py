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


class ourteam(Basepage):
    our_team = (By.XPATH, "//li[@id='menu-item-13938']")
    title = (By.XPATH, "//a[@title='Annalect']")
    find_career = (By.XPATH, "//a[contains(text(),'Find Careers in the US')]")
    across_globe = (By.XPATH, "//a[contains(text(),'Across the Globe')]")
    instagram = (By.XPATH, "//a[contains(text(),'Instagram')]")
    img = (By.CSS_SELECTOR, ". ls-is-cached lazyloaded")
    imgg = (By.XPATH, "//img")
    imggg = (By.CLASS_NAME, " ls-is-cached")
    know_them = (By.XPATH, "//a[contains(text(),'Get to Know Them')]")
    leader_img = (By.CLASS_NAME, "vc_gitem-link")
    blog_img = (By.XPATH, "(//div[@class='vc_gitem-zone vc_gitem-zone-a vc_custom_1708112172958 vc_gitem-is-link lazyloaded'])[1]")
    blog_title = (By.XPATH, "(//a[@class='vc_gitem-link'])[2]")
    read_more = (By.XPATH, "(//a[contains(text(),'Read more')])[3]")
    blog_headline = (By.CSS_SELECTOR, ".page-title.entry-title")
    blog_category = (By.CSS_SELECTOR, ".post-meta-categories")

    def Our_team(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)

    def Find_career(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)
        self.hrm_btn_click(self.find_career)

    def Across_globe(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)
        self.hrm_btn_click(self.across_globe)

    def Instagram(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)
        self.hrm_btn_click(self.instagram)

    def Images(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)

        image_elements = self.hrm_visibility_elements(self.imggg)

        alt_texts = []
        for img in image_elements:
            alt_text = img.get_attribute("alt")
            if alt_text:  # Only add non-empty alt texts
                alt_texts.append(alt_text)

        # Print all collected alt texts
        for i, text in enumerate(alt_texts, 1):
            print(f"Image {i}: {text}")

    def Get_to_know_them(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)
        self.hrm_btn_click(self.know_them)

    def Leadership(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.our_team)
        actions = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0,1000);")  # Scroll to blog section

        self.hrm_visibility_elements(self.leader_img)
        leader_elements = self.driver.find_elements(*self.leader_img)

        names = []
        for i, leader in enumerate(leader_elements[:10], 1):  # Limit to first 10 elements
            actions.move_to_element(leader).perform()  # Hover over the element
            name = leader.get_attribute("title")  # Get the name from the title attribute
            if name:  # Check if the name is not empty
                names.append(name)
                print(f"Leader name {i}: {name}")
        print(names)

        name_list = ("Slavi Samardzija", "Adam Gitlin", "Clarissa Season", "Lauren Walker",
                     "Steve Tobengauz", "Jon Ghazi", "Anna Nicanorova", "Art Schram",
                     "Mark Reggimenti", "James Aylett")

        for i, name in enumerate(names):
            if name == name_list[i]:
                print(f"The Leader {i} {name} matches the names present in name_list {name_list[i]}")
            else:
                print(f"The Leader {i} {name} dot not match the names present in name_list {name_list[i]}")

    def Blog_navigate_and_verify(self, element_locator):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.our_team)
        self.driver.execute_script("window.scrollTo(0,1400);")  # Scroll to blog section
        self.hrm_btn_click(element_locator)
        headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
        print(f"The Headline of the Blog:={headline}")
        category = self.hrm_get_text_element(self.blog_category)  # Get category
        print(f"The blog is from category:={category}")
        return bool(headline) and bool(category)
