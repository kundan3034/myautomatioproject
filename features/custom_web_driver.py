from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

class CustomWebDriver(FirefoxWebDriver, ChromeWebDriver,RemoteWebDriver):
    def __init__(self, profile_directory=None, **kwargs):
        firefox_profile = kwargs.get('firefox_profile')
        FirefoxWebDriver.__init__(self, profile_directory, executable_path = '/usr/local/bin/geckodriver')