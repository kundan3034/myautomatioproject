from selenium import webdriver
import os
from features.custom_web_driver import CustomWebDriver

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from selenium.webdriver.chrome.options import Options



def get_driver(context):
    # profile = FirefoxProfile("ff-profile")

    # context.browser = CustomWebDriver()
    if os.path.exists('/usr/local/bin/chromedriver'):
        print("Chromedriver Path successfully taken")
        opts = Options()
        opts.binary_location = '/usr/local/bin/chromedriver'
        context.browser = webdriver.Chrome(chrome_options=opts)
        # context.browser = webdriver.Chrome('/usr/local/bin/chromedriver')

    else:
        print("Else Path successfully taken")
        context.browser = webdriver.Chrome('/usr/bin/chromedriver')
    # context.browser = webdriver.Firefox()
        #test
        #test test



def before_scenario(context, scenario):
    get_driver(context)
    # screen_width = context.browser.execute_script(
    #     "res=screen.width; return res")
    # screen_height = context.browser.execute_script(
    #     "res=screen.height; return res")
    # context.browser.set_window_size(screen_width, screen_height)
    # context.browser.implicitly_wait(5)  # seconds
    # context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()