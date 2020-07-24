from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Browser:

    @staticmethod
    def create_new_driver(self):
        return webdriver.Chrome()
    
    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()