from .base_page import BasePage
from .locators import LoginPageLocators as L


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert L.LOGIN_LINK_CONTAINS in self.browser.current_url, \
            f"URL does not contain {L.LOGIN_LINK_CONTAINS}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*L.LOGIN_FORM), \
            "Login form doesn't present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*L.REGISTER_FORM), \
            "Register form doesn't present"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*L.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        reg_pas1 = self.browser.find_element(*L.REGISTRATION_PASSWORD1)
        reg_pas1.send_keys(password)
        reg_pas2 = self.browser.find_element(*L.REGISTRATION_PASSWORD2)
        reg_pas2.send_keys(password)
        reg_button = self.browser.find_element(*L.REGISTRATION_BUTTON)
        reg_button.click()
        self.should_be_authorized_user()