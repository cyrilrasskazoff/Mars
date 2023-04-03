from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "admin" in self.driver.current_url, "This is not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def login_admin_and_navigate_to_artists_page(self):
        email = "selwebadmin@test.com"
        password = "Testtest1!"
        email_input = self.driver.find_element(*LoginPageLocators.EMAIL)
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()



