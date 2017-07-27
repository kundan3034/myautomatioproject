from behave import *
from hamcrest import assert_that

from features.steps.pages.search_page import SearchPage


@given('I open google')
def open_google(context):
    context.browser.get("https://www.google.com")


@when('I search for "{keyword}"')
def search_for(context, keyword):
    search_page = SearchPage(context)
    search_page.search_for_keyword(keyword)


@then('I should see "{search_result}" in search result')
def validate_search_result(context, search_result):
    search_page = SearchPage(context)
    results = search_page.get_search_result()
    first_result = results[0]
    print("this is result")
    print(results)
    assert_that(search_result in first_result)