# this file will have method for edition, button ,lnk
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def hrm_send_keys(self, locators, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locators)).send_keys(text)

    def hrm_btn_click(self, locators):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locators)).click()

    def hrm_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def hrm_get_url(self):
        return self.driver.current_url

    def hrm_click_link(self, locators):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locators)).click()

    def hrm_visibility_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def hrm_visibility_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))

    def hrm_get_text_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text


