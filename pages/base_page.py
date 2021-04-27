from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators as B
import random
import string


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout = 10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self, user_is_logged):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        if not user_is_logged:
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*B.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*B.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*B.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*B.USER_ICON), "User icon is not presented,"\
                                                      " probably unauthorised user"

    def logout(self):
        link = self.browser.find_element(*B.LOGOUT_LINK)
        link.click()
        self.should_be_login_link()

    def random_line(self, length):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(length)])