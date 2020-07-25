from Pages.BasePage import BasePage
from Pages.UI_Element import UI_Element
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    # Page basic info
    TITLE = "LinkedIn: Log In or Sign Up"
    URL = ""

    # Page's WebElement(s)
    SIGN_IN_BTN = UI_Element(By.CSS_SELECTOR,"a.nav__button-secondary")

    def __init__(self):
        super().__init__(HomePage.TITLE, \
                         HomePage.URL)
    
    def click_sign_in(self):
        self.SIGN_IN_BTN.click()

        from Pages.LoginPage import LoginPage
        return LoginPage()