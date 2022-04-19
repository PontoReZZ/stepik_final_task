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

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        self.solve_quiz_and_get_code()

    def check_product_name_on_page_with_cart(self):
        product_name_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        assert product_name_in_page == product_name_in_cart, "Incorrect product name"

    def check_product_price_on_page_with_cart(self):
        product_price_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE).text
        assert product_price_in_page == product_price_in_cart, "Incorrect product price"