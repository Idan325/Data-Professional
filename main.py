import json
import time
from random import randrange

import selenium.common.exceptions as ex
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages import HomePage, LoginPage, FeedPage, JobsSearchPage, JobsResultsPage

def get_text_excluding_children(driver, element):
    text = driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)
    return text

# FILTER_SEARCH = False
# TIMEOUT_SEC = 1000
# DRIVER_PATH = '/home/idan/Documents/Infinity/Dev/chromedriver'
# URL = "https://linkedin.com"
# PROXY = ""
# JOB_TITLE = "data analyst"

# with open('proxies.json') as proxy_ips_file:
#     ip_addresses = json.load(proxy_ips_file)

#     index = randrange(0, len(ip_addresses['proxy_ips']))
#     PROXY = ip_addresses['proxy_ips'][index]

# chrome_options = webdriver.ChromeOptions()
## Uncomment to use Proxy for request
#chrome_options.add_argument('--proxy-server=%s' % PROXY)


################ New Driver Code ################
home_page = HomePage.HomePage()
home_page.open()

login_page = home_page.click_sign_in()
feed_page = login_page.perform_sign_in("idan325@gmail.com", "pmqzUBEV795@")
feed_page.minimize_message_window()
jobs_search_page = feed_page.navigate_to_jobs()

jobs_results = jobs_search_page.perform_search("automation", "Israel")

# TODO Check if jobs are correctly retrieved
jobs = jobs_results.get_job_cards
################################################   