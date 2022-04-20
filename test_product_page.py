import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


main_link = "http://selenium1py.pythonanywhere.com"
product_link = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207", 
                "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
                ]
login_link = "https://selenium1py.pythonanywhere.com/ru/accounts/login"

@pytest.mark.need_review
@pytest.mark.parametrize("promo_offer", [pytest.param(i, marks=pytest.mark.xfail(i==7, reason="")) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"{product_link[0]}/?promo=offer{promo_offer}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page_before_add_to_cart()
    product_page.add_to_cart()
    product_page.should_be_product_page_after_add_to_cart()
    product_page.check_product_name_on_page_with_cart()
    product_page.check_product_price_on_page_with_cart()

@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_link[0]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = product_link[0]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_link[0]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_info_message_after_closing()

@pytest.mark.xfail(reason= "Don't work close button")
def test_guest_closes_success_message(browser):
    link = product_link[0]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page_before_add_to_cart()
    product_page.add_to_cart()
    product_page.should_be_product_page_after_add_to_cart()
    product_page.check_product_name_on_page_with_cart()
    product_page.check_product_price_on_page_with_cart()
    product_page.closes_info_message()
    product_page.should_not_be_info_message_after_closing()

def test_guest_should_see_login_link_on_product_page(browser):
    link = product_link[1]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = product_link[1]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = product_link[1]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_text_about_basket_is_empty()

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = login_link
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user("email", "password")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = product_link[0]
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page_before_add_to_cart()
        product_page.add_to_cart()
        product_page.should_be_product_page_after_add_to_cart()
        product_page.check_product_name_on_page_with_cart()
        product_page.check_product_price_on_page_with_cart()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = product_link[0]
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
