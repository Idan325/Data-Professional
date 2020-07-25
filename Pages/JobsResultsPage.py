from Pages.BasePage import BasePage
from Pages.UI_Element import UI_Element
from selenium.webdriver.common.by import By

class JobsResultsPage(BasePage):

    # Page basic info
    TITLE = ""      
    URL = ""

    # Page's WebElement(s)
    PAGE_NAV = UI_Element(By.XPATH, "//div[contains(@class, 'pagination')]")
    JOB_CARDS = UI_Element(By.XPATH, "//div[contains(@class,'job-card-container relative')]")

    jobs = None

    def __init__(self, job_title, job_location):

        JobsResultsPage.TITLE = "{title} Jobs in {location} | LinkedIn" \
                                .format(title = job_title, location = job_location)
        JobsResultsPage.URL = "/jobs/search/?geoId=101620260&keywords={title}   \
                               &location={location}".format(title = job_title, location = job_location)

        super().__init__(JobsResultsPage.TITLE, 
                         JobsResultsPage.URL)        

    def get_job_cards(self):

        self.PAGE_NAV.scroll_into_view()
        return self.JOB_CARDS.get_all_elements()

        # TODO Change to next page, and uncomment when implemented
        # from Pages.FeedPage import FeedPage
        # return FeedPage()