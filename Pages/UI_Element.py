import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Browser import Browser

class UI_Element:

    def __init__(self, by, locator):
        self.by = by
        self.locator = locator    

    def get_element(self, wait=10):
        self.wait_to_appear(wait)
        Browser.get_driver().find_element(self.by, self.locator)

    def get_all_elements(self, wait=10):
        self.wait_to_appear(wait)
        Browser.get_driver().find_elements(self.by, self.locator)

    def get_locator(self):
        return self.locator

    def get_text(self, encoding = None):
        text = self.get_element().text
        return text.encode(encoding) if encoding else text
    
    def get_attribute(self, value):
        return self.get_element().get_attribute(value)

    def is_element_condition(self, expected_condition):
        try:
            WebDriverWait(Browser.get_driver(), 1).until(expected_condition((self.by, self.locator)))
            return True
        except:
            return False

    def exists_in_dom(self):
        return self.is_element_condition(EC.presence_of_element_located)

    def is_selected(self):
        return self.get_element().is_selected()

    def is_checked(self):
        return Browser.get_driver().execute_script("return arguments[0].checked", self.get_element())

    def is_clickable(self):
        return self.exists_in_dom and self.is_element_condition(EC.element_to_be_clickable)


    def wait_to_be_condition(self, expected_condition, timeout = 10):
        start_time = time.time()

        while ((time.time() - start_time) < timeout):
            if self.is_element_condition(expected_condition):
                return self
            time.sleep(1)
        
             
    def wait_to_be_clickable(self, timeout=10):
        return self.wait_to_be_condition(EC.element_to_be_clickable, timeout)

    def wait_to_appear(self, timeout=10):
        return self.wait_to_be_condition(EC.visibility_of_element_located, timeout)

    def wait_to_be_invisible(self, timeout=10):
        return self.wait_to_be_condition(EC.invisibility_of_element_located, timeout)