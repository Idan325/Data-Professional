from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as ex

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


FILTER_SEARCH = False
TIMEOUT_SEC = 20
DRIVER_PATH = '/home/idan/Documents/Infinity/Dev/chromedriver'
URL = "https://linkedin.com"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)
driver.maximize_window()

assert "LinkedIn" in driver.title

try:
    # Wait for 'Sign in" button and click on it
    wait = WebDriverWait(driver, TIMEOUT_SEC)
    eleSignInBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.nav__button-secondary")))
    
    eleSignInBtn.click()

    assert "LinkedIn Login" in driver.title

    # Fill in username and password values
    actions = ActionChains(driver)

    ele_username_input = driver.find_element(By.ID, "username")
    ele_username_input.clear()
    actions.send_keys_to_element(ele_username_input, "idan325@gmail.com")

    ele_pass_input = driver.find_element(By.ID, "password")
    ele_pass_input.clear()
    actions.send_keys_to_element(ele_pass_input, "qazOKM14@#")
    actions.perform()
    actions.reset_actions()

    # Perform Sign In action
    ele_sign_in_btn = driver.find_element_by_xpath("//button[@type='submit']") 
    ele_sign_in_btn.click()

    # Search for jobs in main page
    ele_msg_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[contains(@class, 'msg-overlay')]")))

    if ("overlay.minimize_connection_list_bar" == ele_msg_header.get_attribute("data-control-name")):
        ele_msg_header.click()

    ele_search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember41 > input[class*='search-global']")))
    ele_search_input.clear()
    ele_search_input.send_keys("data analyst")

    ele_search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'search-global-typeahead')]")))
    ele_search_btn.click()
    
    if (True == FILTER_SEARCH):
        filter_search_results()

    # Get search results as elements list. Extract the header element in each and click,
    # extract data and go back

    # div tag: [@class='search-result__info pt3 pb4 ph0']
    # a tag with data-control-name 'search_srp_result'

    # list result element: ul tag with 'search-results__list' in class
    # each result: a tag with a href, click the value (link)
    #search_results = driver.find_elements(By.XPATH, "//a[@data-control-name='search_srp_result']")
    search_results = driver.find_elements(By.XPATH, "//*[contains(@class, 'search']")
    print("Done")

    #for result in search_results:

except ex.NoSuchElementException as e:
    print("Not found: " + e.msg)
except ex.ElementNotInteractableException as e:
    print("Cannot interact: " + e.msg) 