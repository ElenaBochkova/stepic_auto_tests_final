from .base_page import BasePage
from .locators import ProductPageLocators as P


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*P.ADD_PRODUCT_TO_BASKET)
        button.click()

    def check_product_name_alert(self):
        alerts = self.browser.find_elements(*P.ALERT_MESSAGES)
        product_alert = alerts[0].text
        assert self.browser.find_element(*P.PRODUCT_NAME).text == product_alert, \
            "Product name isn't the same at link " + self.browser.current_url

    def check_basket_sum_in_alert(self):
        alerts = self.browser.find_elements(*P.ALERT_MESSAGES)
        basket_sum_in_alert = alerts[2].text
        assert self.browser.find_element(*P.PRODUCT_PRICE).text == basket_sum_in_alert, \
            "Basket sum isn't equal to product price at link " + self.browser.current_url

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*P.ALERT_MESSAGES), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_element_present(*P.ALERT_MESSAGES), \
            "There is no success messages"
        assert self.is_disappeared(*P.ALERT_MESSAGES), \
            "Success message is presented, but should disappear"