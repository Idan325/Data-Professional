from selenium import webdriver

DRIVER_PATH = '/home/idan/Documents/Infinity/Dev/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
##driver.get('https://google.com')

driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

eleUserMessage = driver.find_element_by_id("user-message")
eleUserMessage.clear()
eleUserMessage.send_keys("Test Python")

eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()
