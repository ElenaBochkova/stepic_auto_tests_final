from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK_CONTAINS = "/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_MESSAGES = (By.CSS_SELECTOR, ".alertinner  strong")


class BasketPageLocators():
    TOTAL_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "th.total")
    EMPTY_BASKET_TEXT = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Your basket is empty.")]')