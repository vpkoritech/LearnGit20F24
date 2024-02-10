from selenium import webdriver

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def teardown_module(module):
    driver.quit