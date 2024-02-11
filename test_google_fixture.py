from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("---------Setup----------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    print("---------Teardown----------")
    yield
    driver.quit


def test_google_tite(init_driver):
    assert driver.title == "Google"


def test_google_url(init_driver):
    assert driver.current_url =="https://www.google.com/"

@pytest.mark.usefixtures('init_driver')
def test_google_search():
    searchEnable = driver.find_element(By.XPATH,"//*[@title='Search']").is_displayed()
    print(f"Search Exist? : {searchEnable}")
    print("-----Enable---")
    assert searchEnable==True
