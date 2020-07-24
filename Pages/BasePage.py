from Pages.Browser import Browser

class BasePage:

    DOMAIN = "mydomain.com"

    def __init__(self, expected_title, expected_url, domain=None):
        self.expected_title = expected_title
        self.expected_url = "{domain} {expected_url}".format(domain=domain if domain else DOMAIN, 
                                                             expected_url=expected_url)

    def get_current_url(self):
        return Browser.get_driver().get_current_url()

    def get_title(self):
        return Browser.get_driver().title
    
    def open(self):
        Browser.get_driver().get(self.expected_url)
        return self