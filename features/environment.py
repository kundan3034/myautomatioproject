from selenium import webdriver


def get_driver(context):
    context.browser = webdriver.Firefox()


def before_scenario(context, scenario):
    get_driver(context)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()