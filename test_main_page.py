import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


main_link = "http://selenium1py.pythonanywhere.com"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, main_link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, main_link)
        main_page.open()
        main_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, main_link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_text_about_basket_is_empty()
