import pytest
from selenium import webdriver

""" A fixture that initializes a Chrome driver for a test class.
    """
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver= webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()

@pytest.mark.usefixtures("init_chrome_driver")
class  Base_Chrome_Test:
    pass

class Test_google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures("init_ff_driver")
class  Base_FF_Test:
    pass

class Test_google_FF(Base_FF_Test):
    def test_ff_title_google(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"