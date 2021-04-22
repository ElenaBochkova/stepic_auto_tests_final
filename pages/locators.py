from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK_CONTAINS = "/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_MESSAGES = (By.CSS_SELECTOR, ".alertinner  strong")


class BasketPageLocators():
    TOTAL_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "th.total")
    EMPTY_BASKET_TEXT = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Your basket is empty.")]')