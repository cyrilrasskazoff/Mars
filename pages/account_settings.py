from .base_page import BasePage
from .locators import AccountSettingsLocators


class AccountSettingsPage(BasePage):
    def should_be_account_settings_page(self):
        self.should_be_account_settings_page_title()
        self.should_be_account_settings_url()

    def should_be_account_settings_page_title(self):
        assert self.is_element_present(*AccountSettingsLocators.ACCOUNT_SETTINGS_PAGE_TITLE), "This is not an Account " \
                                                                                              "Settings page "

    def should_be_account_settings_url(self):
        assert "settings" in self.driver.current_url, "This is not an Account Settings page"
