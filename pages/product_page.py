from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page_before_add_to_cart(self):
        self.should_be_add_to_cart_button()
        self.should_be_product_name_on_page()
        self.should_be_product_price_on_page()

    def should_be_product_page_after_add_to_cart(self):
        self.should_be_product_name_in_cart()
        self.should_be_product_price_in_cart()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Button of adding to cart is not presented"

    def should_be_product_name_on_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_name_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_NAME), "Product name in cart is not presented"

    def should_be_product_price_on_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_product_price_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price in cart is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_info_message_after_closing(self):
        assert self.is_disappeared(*ProductPageLocators.CLOSE_INFO_MESSAGE), "Info-message is presented, but should not be"

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        try:
            self.solve_quiz_and_get_code()
        except:
            return False

    def check_product_name_on_page_with_cart(self):
        product_name_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        assert product_name_in_page == product_name_in_cart, "Incorrect product name"

    def check_product_price_on_page_with_cart(self):
        product_price_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE).text
        assert product_price_in_page == product_price_in_cart, "Incorrect product price"

    def closes_info_message(self):
        button_close = self.browser.find_element(*ProductPageLocators.CLOSE_INFO_MESSAGE)
        button_close.click()