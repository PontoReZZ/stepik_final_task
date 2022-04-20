from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") 

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    CLOSE_INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info > a.close")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) > .alertinner > strong")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "basket-title")
    TEXT_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")