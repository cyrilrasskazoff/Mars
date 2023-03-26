from .base_page import BasePage
from .locators import AdminUsersLocators


class AdminUsersPage(BasePage):
    def should_be_admin_users_page(self):
        self.should_be_admin_users_page_title()
        self.should_be_admin_users_url()

    def should_be_admin_users_page_title(self):
        assert self.is_element_present(*AdminUsersLocators.ADMIN_USERS_PAGE_TITLE), "This is not an Admin " \
                                                                                    "Users page"

    def should_be_admin_users_url(self):
        assert "admin-users" in self.driver.current_url, "This is not an Admin Users page"
