from selenium import webdriver
import pytest

driver = None

def setup_module(mod):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def teardown_module(mod):
    driver.quit


def test_google_tite():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url =="https://www.google.com/"


