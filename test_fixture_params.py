import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param=="chrome":
        web_driver = webdriver.Chrome()
    elif request.param=='firefox':
        web_driver = webdriver.Firefox()
    else:
        print("Enter correct driver ")
    request.cls.driver= web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class Base_Google():
    pass
class Test_Chrome_Google(Base_Google):
    def test_chrome_google_Title(self):

        self.driver.get("https://google.com")
        assert self.driver.title=='Google'


    def test_chrome_google_url(self):

        self.driver.get("https://google.com")
        assert self.driver.current_url=='https://www.google.com/'
