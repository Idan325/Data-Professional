import json
from random import randrange

import selenium.common.exceptions as ex
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def filter_search_results():
    # Choose jobs filter parameters
    ele_all_filters = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-control-name='all_filters']")))
    ele_all_filters.click()

    # Wait for elements to be refreshed on DOM
    driver.implicitly_wait(5)

    # Choose job posting period
    ele_job_param = driver.find_element(By.ID, "sf-timePostedRange-r2592000")
    driver.execute_script("arguments[0].click()", ele_job_param)

    # Check possible job locations
    ele_job_param = driver.find_element(By.ID, "sf-populatedPlace-100908386")
    driver.execute_script("arguments[0].click()", ele_job_param)

    ele_job_param = driver.find_element(By.ID, "sf-populatedPlace-105752964")
    driver.execute_script("arguments[0].click()", ele_job_param)

    ele_job_param = driver.find_element(By.ID, "sf-populatedPlace-105269768")
    driver.execute_script("arguments[0].click()", ele_job_param)

    # Check relevant job types
    ele_job_param = driver.find_element(By.ID, "sf-jobType-F")
    driver.execute_script("arguments[0].click()", ele_job_param)

    ele_job_param = driver.find_element(By.ID, "sf-jobType-I")
    driver.execute_script("arguments[0].click()", ele_job_param)

    # Choose job functions
    ele_job_param = driver.find_element(By.ID, "sf-function-anls")
    driver.execute_script("arguments[0].click()", ele_job_param)

    ele_job_param = driver.find_element(By.ID, "sf-function-eng")
    driver.execute_script("arguments[0].click()", ele_job_param)

    # Choose experience levels
    ele_job_param = driver.find_element(By.ID, "sf-experience-1")
    driver.execute_script("arguments[0].click()", ele_job_param)

    ele_job_param = driver.find_element(By.ID, "sf-experience-2")
    driver.execute_script("arguments[0].click()", ele_job_param)

    # Apply search filters
    ele_job_param = driver.find_element(By.XPATH, "//button[contains(@class,'button--apply')]")
    driver.execute_script("arguments[0].click()", ele_job_param)

def get_text_excluding_children(driver, element):
    text = driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)
    return text

FILTER_SEARCH = False
TIMEOUT_SEC = 1000
DRIVER_PATH = '/home/idan/Documents/Infinity/Dev/chromedriver'
URL = "https://linkedin.com"
PROXY = ""
JOB_TITLE = "data analyst"

with open('proxies.json') as proxy_ips_file:
    ip_addresses = json.load(proxy_ips_file)

    index = randrange(0, len(ip_addresses['proxy_ips']))
    PROXY = ip_addresses['proxy_ips'][index]

chrome_options = webdriver.ChromeOptions()
## Uncomment to use Proxy for request
#chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)

wait = WebDriverWait(driver, TIMEOUT_SEC)

driver.get(URL)
driver.set_window_size(width=810, height=900)

wait.until(EC.title_contains, "LinkedIn")

try:

    # Wait for 'Sign in" button and click on it    
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.nav__button-secondary")))    
    sign_in_btn.click()

    wait.until(EC.title_contains, "LinkedIn Login")

    # Fill in username and password
    actions = ActionChains(driver)

    ele_username_input = driver.find_element(By.ID, "username")
    ele_username_input.clear()
    actions.send_keys_to_element(ele_username_input, "idan325@gmail.com")

    ele_pass_input = driver.find_element(By.ID, "password")
    ele_pass_input.clear()    
    actions.send_keys_to_element(ele_pass_input, "pmqzUBEV795@")
    actions.perform()
    actions.reset_actions()

    # Perform Sign In action
    ele_sign_in_btn = driver.find_element_by_xpath("//button[@type='submit']") 
    ele_sign_in_btn.click()

    # Minimize message pop-up
    ele_msg_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[contains(@class, 'msg-overlay')]")))

    if ("overlay.minimize_connection_list_bar" == ele_msg_header.get_attribute("data-control-name")):
        ele_msg_header.click()

    # Navigate to Jobs from main nav.
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/jobs/']"))).click()

    wait._timeout = 20
    wait.until(EC.title_contains, "Jobs | LinkedIn")
    wait._timeout = TIMEOUT_SEC

    # Search for jobs in wanted position 
    actions = ActionChains(driver)

    wait._timeout = 20
    job_title_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'jobs-search-box-keyword-id')]")))
    wait._timeout = TIMEOUT_SEC

    job_title_input.clear()
    actions.send_keys_to_element(job_title_input, JOB_TITLE)

    job_location_input = driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id')]")
    job_location_input.clear()
    actions.send_keys_to_element(job_location_input, "Israel")

    job_search_btn = driver.find_element_by_css_selector("button[class*='jobs-search-box__submit-button']")
    actions.click(job_search_btn)

    driver.implicitly_wait(3)
    actions.perform()
    actions.reset_actions()

    # Get search results as elements list. Extract the header element in each and click,
    # extract data and go back

    wait.until(EC.title_is(JOB_TITLE + ' Jobs in Israel | LinkedIn'))
        
    jobs_div = driver.find_element_by_xpath("//div[contains(@class,'--is-two-pane')]")
    

    # Scroll down job cards (move to bottom page nav.)
    page_nav = driver.find_element_by_xpath("//div[contains(@class, 'pagination')]")
    driver.execute_script("return arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", page_nav)


    job_cards_left_pane = driver.find_elements_by_xpath("//div[contains(@class,'job-card-container relative')]")

    
    print("Checkpoint")
    



    
    #! Old code below (elements unavailable)
    # driver.implicitly_wait(10)
    # search_results = driver.find_elements(By.XPATH, "//div[contains(@class,'search-result__info')]/child::a[1]")

    # actions.reset_actions()

    # res_file = open("results.txt", 'a')

    # actions = ActionChains(driver)

    # for result in search_results: 
        
    #     ActionChains(driver) \
    #         .key_down(Keys.CONTROL) \
    #         .click(result)  \
    #         .key_up(Keys.CONTROL)  \
    #         .perform()

    #     driver.switch_to_window(driver.window_handles[1])
    #     see_more_btn = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='See more']")))
    #     see_more_btn.click()

    #     job_details = wait.until(EC.visibility_of_element_located((By.ID, "job-details")))      

    #     # Print span text_content      
    #     print(get_text_excluding_children(driver, job_details)) 

    #     print("New Tab")

    # res_file.close()

except ex.TimeoutException as e:
    print("Time's up: " + e.msg)
except ex.NoSuchElementException as e:
    print("Not found: " + e.msg)
except ex.ElementNotInteractableException as e:
    print("Cannot interact: " + e.msg) 
