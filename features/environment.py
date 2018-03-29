from selenium import webdriver
import os
from features.custom_web_driver import CustomWebDriver

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from selenium.webdriver.chrome.options import Options



def get_driver(context):
    # profile = webdriver.FirefoxProfile()
    # profile.native_events_enabled = True
    # context.browser = webdriver.Firefox(profile)
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')




def before_scenario(context, scenario):
    get_driver(context)
    # screen_width = context.browser.execute_script(
    #     "res=screen.width; return res")
    # screen_height = context.browser.execute_script(
    #     "res=screen.height; return res")
    # context.browser.set_window_size(screen_width, screen_height)
    context.browser.implicitly_wait(5)  # seconds
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()