from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "Incorrect url"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product on basket is presented, but should not be"

    def should_be_text_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_BASKET_IS_EMPTY), "Dont't have text about basket, but should be"
