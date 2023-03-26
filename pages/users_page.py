from .base_page import BasePage
from .locators import UsersPageLocators
from selenium.webdriver.common.keys import Keys


class UsersPage(BasePage):
    def should_be_users_page(self):
        self.should_be_users_page_title()
        self.should_be_users_url()

    def should_be_users_page_title(self):
        assert self.is_element_present(*UsersPageLocators.USERS_PAGE_TITLE), "This is not a Users page"

    def should_be_users_url(self):
        assert "users" in self.driver.current_url, "This is not a Users page"

    def should_filter_by_individual_account_type_work(self):
        account_type_filter = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER).click()
        individual_account_option = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER_INDIVIDUAL).click()
        individual_filter_results = self.driver.find_elements(*UsersPageLocators.INDIVIDUAL_FILTER_RESULTS)
        for result in individual_filter_results:
            assert "Individual" in result.text and "Entity" not in result.text, "Individual Filter failed"

    def should_filter_by_entity_account_type_work(self):
        account_type_filter = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER).click()
        entity_account_option = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER_ENTITY).click()
        entity_filter_results = self.driver.find_elements(*UsersPageLocators.ENTITY_FILTER_RESULTS)
        for result in entity_filter_results:
            assert "Entity" in result.text and "Individual" not in result.text, "Entity Filter failed"

    def should_filter_by_email_work(self):
        email = UsersPageLocators.email
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(email)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        email_filter_results = self.driver.find_elements(*UsersPageLocators.EMAIL_FILTER_RESULTS)
        for result in email_filter_results:
            assert email == result.text, "Filter by Email failed"

    def should_filter_by_name_work(self):
        name = UsersPageLocators.name
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(name)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        name_filter_results = self.driver.find_elements(*UsersPageLocators.NAME_FILTER_RESULTS)
        for result in name_filter_results:
            assert name == result.text, "Filter by Name failed"

    def should_navigate_user_to_user_details_page(self):
        email = UsersPageLocators.email
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(email)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        self.driver.find_element(*UsersPageLocators.EMAIL_FILTER_RESULT).click()
