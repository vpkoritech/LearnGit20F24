import time
from selenium import webdriver
import pytest

def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google"==driver.title
    time.sleep(5)
    driver.quit

def test_facebook():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    assert "Facebook – log in or sign up"==driver.title
    time.sleep(5)
    driver.quit

def test_IBM():
    driver = webdriver.Chrome()
    driver.get("https://www.ibm.com/in-en/careers")
    assert "Define your career with IBM"==driver.title
    time.sleep(5)
    driver.quit

def test_Apple():
    driver = webdriver.Chrome()
    driver.get("https://www.apple.com/in/")
    assert "Apple (India)"==driver.title
    time.sleep(5)
    driver.quit

def test_Crest():
    driver = webdriver.Chrome()
    driver.get("https://www.crestdatasys.com/careers/job-openings/")
    assert "Job Openings - Crest Data Systems"==driver.title
    time.sleep(5)
    driver.quit

