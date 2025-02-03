# Import all the necessary libraries
import time  # for time delay
import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions


class ahomepage(Basepage):
    meet_omni = (By.XPATH, "//*[contains(text(),'Meet Omni')]")
    meet_omni_video = (By.XPATH, "//video[@class='omni-home-video']")
    cookies = (By.XPATH, "//*[contains(text(),'Accept All Cookies')]")
    title = (By.XPATH, "//a[@title='Annalect']")
    dpm = (By.XPATH, "//*[contains(text(),'Discover How')]")
    fpt = (By.XPATH, "//*[contains(text(),'Explore Solutions')]")
    blog_img = (By.XPATH, "(//div[@class='item-image post-media'])[1]")
    blog_category = (By.CSS_SELECTOR, ".post-meta-categories")
    blog_headline = (By.CSS_SELECTOR, ".page-title.entry-title")
    blog_title = (By.XPATH, "(//h2[@class='post-title entry-title'])[2]")
    read_more = (By.XPATH, "(//a[@class='more-link'])[3]")
    career = (By.XPATH, "//*[contains(text(),'Careers')]")
    leadership = (By.XPATH, "//*[contains(text(),'Leadership')]")
    press = (By.XPATH, "//*[contains(text(),'Press')]")
    location = (By.XPATH, "//*[contains(text(),'Locations')]")
    contact = (By.XPATH, "//*[contains(text(),'Contact Us')]")
    privacy = (By.XPATH, "(//*[contains(text(),'Your Privacy Choices')])[1]")
    accept = (By.CSS_SELECTOR, ".save-preference-btn-handler.onetrust-close-btn-handler")
    notice = (By.XPATH, "(//*[contains(text(),'Privacy Notice')])")
    terms = (By.XPATH, "(//*[contains(text(),'Terms of Use')])")
    support = (By.XPATH, "(//*[contains(text(),'Omni Support')])")
    instagram = (By.XPATH, "//a[@class='a13_soc-instagram fa fa-instagram']")
    linkedin = (By.XPATH, "//a[@class='a13_soc-linkedin fa fa-linkedin']")
    twitter = (By.XPATH, "//a[@class='a13_soc-twitter fa fa-twitter']")
    facebook = (By.XPATH, "//a[@class='a13_soc-facebook fa fa-facebook']")
    scrollup = (By.XPATH, "//a[@id='to-top']")
    omni = (By.XPATH, "//li[@id='menu-item-13334']")
    data_power_market = (By.XPATH, "//li[@id='menu-item-14636']")
    future_tech = (By.XPATH, "//li[@id='menu-item-14634']")
    our_team = (By.XPATH, "//li[@id='menu-item-13938']")
    blog = (By.XPATH, "//li[@id='menu-item-15536']")
    search_btn = (By.XPATH, "//button[@id='search-button']")
    search = (By.XPATH, "(//input[@id='s1'])")

    # Method for navigating to the 'Omni' page

    def Meet_omni(self):
        self.hrm_btn_click(self.omni)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "omni" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Omni page ")
            return True  # Indicates test success
        else:
            print("F- The automation is not directed to Omni page")
            return False  # Indicates test failure

    # Method for navigating to the 'Omni' page

    def Meet_omni_video(self):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(self.meet_omni_video)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "omni" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Omni page ")
            return True  # Indicates test success
        else:
            print("F- The automation is not directed to Omni page")
            return False  # Indicates test failure

    # Method for navigating to the 'Data Powered Marketing' page

    def Dpm(self):
        self.hrm_btn_click(self.title)
        self.driver.execute_script("window.scrollTo(0,350);")
        self.hrm_btn_click(self.dpm)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "effectiveness" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Data Powered Marketing page ")
            return True
        else:
            print("F- The automation is not directed to Data Powered Marketing page")
            return False

    # Method for navigating to the 'Future Proofed Tech' page

    def Fpt(self):
        self.hrm_btn_click(self.title)
        self.driver.execute_script("window.scrollTo(0,650);")
        self.hrm_btn_click(self.fpt)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "efficiency" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Future Proofed Tech page ")
            return True
        else:
            print("F- The automation is not directed to Future Proofed Tech page")
            return False

    # Method for navigating to the 'Blog' page

    def Blog_img(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,1400);")  # Scroll to blog section
        self.hrm_btn_click(self.blog_img)
        headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
        print(f"The blog is from category:={headline}")

        category = self.hrm_get_text_element(self.blog_category)  # Get category
        print(f"The blog is from category:={category}")

    # Method for navigating to the 'Blog' page

    def Blog_title(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,1400);")  # Scroll to blog section
        self.hrm_btn_click(self.blog_title)
        headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
        print(f"The blog is from category:={headline}")
        category = self.hrm_get_text_element(self.blog_category)  # Get category
        print(f"The blog is from category:={category}")

    # Method for navigating to the 'Blog' page

    def Blog_Readmore(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,1600);")  # Scroll to section
        self.hrm_btn_click(self.read_more)
        headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
        print(f"The blog is from category:={headline}")
        category = self.hrm_get_text_element(self.blog_category)  # Get category
        print(f"The blog is from category:={category}")

    # Method for navigating to the 'Career' page

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

    # Method for navigating to the 'Leadership' page

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

    # Method for navigating to the 'Press' page

    def Press(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.press)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "press" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Blogs / Press page ")
            return True
        else:
            print("F- The automation is not directed to Blogs / Press page")
            return False

    # Method for navigating to the 'Location' page

    def Location(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.location)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "location" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Location page ")
            return True
        else:
            print("F- The automation is not directed to Location page")
            return False

    # Method for navigating to the 'Contact Us' page

    def Contact(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.contact)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "contact" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Contact page ")
            return True
        else:
            print("F- The automation is not directed to Contact page")
            return False

    # Method for navigating to the 'Privacy Choices' page

    def Privacy(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(self.privacy)
        self.hrm_btn_click(self.accept)

    # Method for navigating to the 'Privacy Notice' page

    def Notice(self):
        self.hrm_btn_click(self.notice)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to current window handle
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "privacy" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Privacy Notice page ")
            result = True
        else:
            print("F- The automation is not directed Privacy Notice page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'Terms of use' page

    def Terms(self):
        self.hrm_btn_click(self.terms)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to current window handle
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "terms" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Terms of use page ")
            result = True
        else:
            print("F- The automation is not directed Terms of use page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'Support' page

    def Support(self):
        self.hrm_btn_click(self.support)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to current window handle
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "servicedesk" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Support page ")
            result = True
        else:
            print("F- The automation is not directed Support page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'Instagram' page

    def Instagram(self):
        self.hrm_btn_click(self.instagram)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "instagram" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Instagram page ")
            result = True
        else:
            print("F- The automation is not directed Instagram page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'LinkedIn' page

    def Linkedin(self):
        self.hrm_btn_click(self.linkedin)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)

        current_url = self.hrm_get_url()  # Retrieves current URL
        if "linkedin" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Linkedin page ")
            result = True
        else:
            print("F- The automation is not directed Linkedin page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'Twitter' page

    def Twitter(self):
        self.hrm_btn_click(self.twitter)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to current window handle
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "linkedin" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Twitter page ")
            result = True
        else:
            print("F- The automation is not directed Twitter page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for navigating to the 'Facebook' page

    def Facebook(self):
        self.hrm_btn_click(self.facebook)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to current window handle
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "facebook" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Facebook page ")
            result = True
        else:
            print("F- The automation is not directed Facebook page")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result

    # Method for Scrolling to Top of the page

    def Scrollup(self):
        time.sleep(5)
        self.hrm_btn_click(self.scrollup)  # Scrolling to Top of the page
        time.sleep(4)

    # Method for navigating to the 'Omni' page

    def Omni(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.omni)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "omni" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Omni page ")
            return True
        else:
            print("F- The automation is not directed to Omni page")
            return False

    # Method for navigating to the 'Data Powered Marketing' page

    def Data_Power_Marketing(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.data_power_market)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "effectiveness" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Data Powered Marketing page ")
            return True
        else:
            print("F- The automation is not directed to Data Powered Marketing page")
            return False

    # Method for navigating to the 'Future Proofed Tech' page

    def Future_Tech(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.future_tech)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "efficiency" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Future Proofed Tech page ")
            return True
        else:
            print("F- The automation is not directed to Future Proofed Tech page")
            return False

    # Method for navigating to the 'Our team' page

    def Our_Team(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.our_team)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "team" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Our Team page ")
            return True
        else:
            print("F- The automation is not directed to Our Team page")
            return False

    # Method for navigating to the 'Blog' page

    def Blog(self):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.blog)
        current_url = self.hrm_get_url()  # Retrieves current URL
        if "blog" in current_url:  # Checks if the URL matches expected text
            print("T- The automation is directed to Blog page ")
            return True
        else:
            print("F- The automation is not directed to Blog page")
            return False

    # Method for navigating to the Search bar and search the content

    def Search(self, text):
        self.hrm_btn_click(self.title)  # Navigate home
        self.hrm_btn_click(self.search_btn)  # click on the search button
        self.hrm_send_keys(self.search, text + Keys.ENTER)  # enter the text , Keys.ENTER - used to click enter key
        time.sleep(5)

########################################################################################

    def navigate_and_verify(self, element_locator, expected_text_in_url):
        self.hrm_btn_click(self.title)
        self.driver.execute_script("window.scrollTo(0,300);")
        self.hrm_btn_click(element_locator)
        current_url = self.hrm_get_url()
        if expected_text_in_url in current_url:
            print(f"T- Navigated successfully to the {expected_text_in_url} page.")
            return True
        else:
            print(f"F- Failed to navigate to the {expected_text_in_url} page.")
            return False

    def Blog_navigate_and_verify(self, element_locator):
        self.hrm_btn_click(self.title)  # Navigate home
        self.driver.execute_script("window.scrollTo(0,1400);")  # Scroll to blog section
        self.hrm_btn_click(element_locator)
        headline = self.hrm_get_text_element(self.blog_headline)  # Get headline
        print(f"The Headline of the blog :={headline}")
        category = self.hrm_get_text_element(self.blog_category)  # Get category
        print(f"The blog is from category:={category}")
        return bool(headline) and bool(category)

    def header_navigate_and_verify(self, element_locator, expected_text_in_url):
        self.hrm_btn_click(self.title)
        self.hrm_btn_click(element_locator)
        current_url = self.hrm_get_url()
        if expected_text_in_url in current_url:
            print(f"T- Navigated successfully to the {expected_text_in_url} page.")
            return True
        else:
            print(f"F- Failed to navigate to the {expected_text_in_url} page.")
            return False

    def corporate_navigate_and_verify(self, element_locator, expected_text_in_url):
        self.hrm_btn_click(self.title)
        self.driver.execute_script("window.scrollTo(0,2500);")  # Scroll to section
        self.hrm_btn_click(element_locator)
        current_url = self.hrm_get_url()
        if expected_text_in_url in current_url:
            print(f"T- Navigated successfully to the {expected_text_in_url} page.")
            return True
        else:
            print(f"F- Failed to navigate to the {expected_text_in_url} page.")
            return False

    def privacy_social_navigate_and_verify(self, element_locator, expected_text_in_url):
        self.hrm_btn_click(element_locator)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.hrm_get_url()
        if expected_text_in_url in current_url:
            print(f"T- Navigated successfully to the {expected_text_in_url} page.")
            result = True
        else:
            print(f"F- Failed to navigate to the {expected_text_in_url} page.")
            result = False

        self.driver.close()  # Close the LinkedIn window
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch to first tab that is main annalect page
        return result


