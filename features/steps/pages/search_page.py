from selenium.webdriver.common.keys import Keys


class SearchPage(object):
    def __init__(self, context):
        self.context = context
        self.driver = context.browser

    def search_for_keyword(self, keyword):
        self.driver.maximize_window()
        search_box = self.driver.find_element_by_css_selector(".gsfi")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)

    def get_search_result(self):
        all_search_results = self.driver.find_elements_by_css_selector(".srg > div")
        text_list = []
        for result in all_search_results:
            text_list.append(result.text)
        return text_list
