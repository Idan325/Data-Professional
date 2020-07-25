import time
from Pages.BasePage import BasePage
from Pages.UI_Element import UI_Element
from selenium.webdriver.common.by import By

class JobsSearchPage(BasePage):

    # Page basic info
    TITLE = "Jobs | LinkedIn"      #! Part of a dynamic title
    URL = "/jobs/?showJobAlertsModal=false"

    # Page's WebElement(s)
    JOB_TITLE = UI_Element(By.XPATH, "//input[contains(@id, 'jobs-search-box-keyword-id')]")
    JOB_LOCATION = UI_Element(By.XPATH, "//input[contains(@id, 'jobs-search-box-location-id')]")
    JOB_SEARCH_BTN = UI_Element(By.CSS_SELECTOR, "button[class*='jobs-search-box__submit-button']")

    def __init__(self):
        super().__init__(JobsSearchPage.TITLE, 
                         JobsSearchPage.URL)

    def enter_job_title(self, title):
        self.JOB_TITLE.type_input(title)

    def enter_job_location(self, location):
        self.JOB_LOCATION.type_input(location)

    def perform_search(self, title, location):
        time.sleep(2)
        self.enter_job_title(title)
        time.sleep(2)
        self.enter_job_location(location)
    
        self.JOB_SEARCH_BTN.click()
        
        from Pages.JobsResultsPage import JobsResultsPage
        return JobsResultsPage(title, location)