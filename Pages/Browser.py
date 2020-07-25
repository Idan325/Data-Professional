from selenium import webdriver
import selenium.common.exceptions as ex
from selenium.webdriver.common.keys import Keys

class Browser:

    CHROME = 1
    EDGE = 2
    FIREFOX = 3
    OPERA = 4
    INTERNET_EXPLORER = 5

    DRIVER_PATH = "/home/idan/Documents/Infinity/Dev/chromedriver"
    driver = None

    #! The 'Options' argument must be compatible with driver type
    @staticmethod
    def get_driver(driver_id = CHROME, 
                   driver_path = DRIVER_PATH,
                   driver_options = None):
        
        def create_new_driver(driver_id, driver_path):
            if (Browser.CHROME == driver_id):
                driver = webdriver.Chrome(executable_path=driver_path, options=driver_options)
            elif (Browser.EDGE == driver_id):
                driver = webdriver.Edge(executable_path=driver_path)
            elif (Browser.FIREFOX == driver_id):
                driver = webdriver.Firefox(executable_path=driver_path, options=driver_options)
            elif (Browser.OPERA == driver_id):
                driver = webdriver.Opera(executable_path=driver_path)
            elif (Browser.INTERNET_EXPLORER == driver_id):
                driver = webdriver.Ie(executable_path=driver_path, options=driver_options)
            else:
                raise Exception("Browser of type {} is not supported".format(driver_id))
            return driver

        if (None == Browser.driver):
            try:
                Browser.driver = create_new_driver(driver_id, driver_path)
            except ex.SessionNotCreatedException as error:
                print("Driver options are not compatible with driver type")
                raise error

        return Browser.driver

    @staticmethod
    def move_to_active_window(self):
        window_handles = Browser.get_driver().window_handles

        if (1 == len(window_handles)):
            Browser.get_driver().switch_to_window(window_handles[0])
            return        
        for window_index in range(1, len(window_handles)):
            Browser.get_driver().switch_to_window(window_handles[-window_index])
            return