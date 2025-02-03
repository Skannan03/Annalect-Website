# Import all the necessary libraries
import time  # for time delay
import pytest  # Framework for writing test cases
from selenium import webdriver  # Automates browser interaction
from utility.baseclass import Basepage  # Custom base class for utilities
from selenium.webdriver.common.by import By  # Used for locating web elements
from selenium.webdriver.common.keys import Keys  # Simulates keyboard actions
from selenium.webdriver.support.wait import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Wait conditions

class contactpage(Basepage):
