from .base_page import BasePage
from .locators import UserDetailsPageLocators


class UserDetailsPage(BasePage):
    def should_be_user_details_page(self):
        self.should_be_user_details_url()
        self.should_be_manage_user_button()

    def should_be_user_details_url(self):
        assert "/users/" in self.driver.current_url, "This is not a User Details Page"

    def should_be_manage_user_button(self):
        assert self.is_element_present(*UserDetailsPageLocators.MANAGE_USER_BUTTON), "Manage User button is missing"