from .base_page import BasePage
from .locators import BasketPageLocators as B


class BasketPage(BasePage):
    def should_no_products(self):
        assert not self.is_element_present(*B.TOTAL_PRODUCTS_IN_BASKET), \
            "There are products in basket that should be empty"

    def there_is_a_text_about_empty_basket(self):
        assert self.is_element_present(*B.EMPTY_BASKET_TEXT), \
            "There is no text about empty basket at all"