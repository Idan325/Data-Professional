from Pages.BasePage import BasePage
from Pages.UI_Element import UI_Element
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):

    # Page basic info
    TITLE = "LinkedIn Login, Sign in | LinkedIn"
    URL = ""

    # Page's WebElement(s)
    USER_NAME_INPUT = UI_Element(By.ID, "username")
    PASSWORD_INPUT = UI_Element(By.ID, "password")
    SIGN_IN_BTN = UI_Element(By.XPATH, "//button[@type='submit']")

    def __init__(self):
        super().__init__(LoginPage.TITLE, 
                         LoginPage.URL)
    
    def enter_username(self, username):
        self.USER_NAME_INPUT.type_input(username)

    def enter_password(self, password):
        self.PASSWORD_INPUT.type_input(password)

    def perform_sign_in(self, username, password):
        time.sleep(2)
        self.enter_username(username)
        time.sleep(2)
        self.enter_password(password)
    
        self.SIGN_IN_BTN.click()
        
        from Pages.FeedPage import FeedPage
        return FeedPage()