from Pages.BasePage import BasePage
from Pages.UI_Element import UI_Element
from selenium.webdriver.common.by import By

class FeedPage(BasePage):

    # Page basic info
    TITLE = "LinkedIn"      #! Part of a dynamic title
    URL = "/feed/?trk=homepage-basic_signin-form_submit"

    # Page's WebElement(s)
    DATA_CTRL_NAME_EXPENDED = "overlay.minimize_connection_list_bar"
    MESSAGE_HEADER = UI_Element(By.XPATH, "//header[contains(@class, 'msg-overlay')]")
    JOBS_NAV = UI_Element(By.XPATH, "//a[@href='/jobs/']")

    def __init__(self):
        super().__init__(FeedPage.TITLE, 
                         FeedPage.URL)
    

    def minimize_message_window(self):
        if (self.DATA_CTRL_NAME_EXPENDED == self.MESSAGE_HEADER.get_attribute("data-control-name")):
            self.MESSAGE_HEADER.click()

    def navigate_to_jobs(self):
        self.JOBS_NAV.click()

        from Pages.JobsSearchPage import JobsSearchPage
        return JobsSearchPage()