import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language for site (default: English)")
    parser.addoption("--headless", action="store_true", default="False", help="Start Chrome with headless mode")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    headless_mode = request.config.getoption("headless")
    options = Options()
    options.add_argument("headless") if headless_mode == True else ''
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
