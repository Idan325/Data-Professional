import time

import selenium.common.exceptions as ex
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
        return Browser.get_driver().find_element(self.by, self.locator)

    def get_all_elements(self, wait=10):
        self.wait_to_appear(wait)
        return Browser.get_driver().find_elements(self.by, self.locator)

    def get_locator(self):
        return self.locator

    def get_text(self, encoding = None):
        text = self.get_element().text
        return text.encode(encoding) if encoding else text
    
    def get_attribute(self, value):
        return self.get_element().get_attribute(value)

    def exists_in_dom(self):
        return ((bool)(self.wait_to_be_present_in_dom()))

    def is_selected(self):
        return self.get_element().is_selected()

    def is_checked(self):
        return Browser.get_driver().execute_script("return arguments[0].checked", self.get_element())

    def is_clickable(self):
        try:
            self.exists_in_dom and (None != self.wait_to_be_clickable())
        except:
            return False

    def wait_to_be_clickable(self, timeout = 10):
        return WebDriverWait(Browser.get_driver(), timeout). \
               until(EC.element_to_be_clickable((self.by, self.locator)))

    def wait_to_appear(self, timeout=10):
        return WebDriverWait(Browser.get_driver(), timeout). \
               until(EC.visibility_of_element_located((self.by, self.locator)))

    def wait_to_be_present_in_dom(self, timeout=10):
        return WebDriverWait(Browser.get_driver(), timeout). \
               until(EC.presence_of_element_located((self.by, self.locator)))

    def wait_to_be_invisible(self, timeout=10):
        return WebDriverWait(Browser.get_driver(), timeout). \
               until(EC.invisibility_of_element_located((self.by, self.locator)))


    def click(self, timeout = 10, action_chains_click = False):
        element = self.wait_to_be_clickable()
        at_begining_handles = Browser.get_driver().window_handles

        if (action_chains_click):
            ActionChains(Browser.get_driver()).click(self.get_element()).perform()
        else:
            try:
                element.click()
            except ex.ElementNotInteractableException as error:
                print("Element isn't interactable")
                raise error
            except ex.StaleElementReferenceException as error:
                print("Stale Element")
                raise error
            except ex.WebDriverException as error:
                print("General exception")
                raise error

        # Move to new active tab if there is one
        if (len(Browser.get_driver().window_handles) > len(at_begining_handles)):
            Browser.move_to_active_window()
        
        return self

    def type_input(self, string, action_chains = False):
        self.wait_to_appear()
        
        if (not action_chains):
            self.get_element().clear()
            self.get_element().send_keys(string)
            return
        
        ActionChains(Browser.get_driver()).send_keys_to_element(self).perform

    def scroll_into_view(self, behavior = "smooth", block = "end"):
        script = "return arguments[0].scrollIntoView({behavior: " \
                 + behavior  + ", block: " + block + "});"
        
        Browser.get_driver().execute_script(script, self)