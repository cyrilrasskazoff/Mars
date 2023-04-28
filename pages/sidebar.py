import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import SidebarLocators


class Sidebar(BasePage):

    def should_be_sidebar_menu(self):
        self.should_be_logo_link()
        self.should_be_artists_link()
        self.should_be_users_link()
        self.should_be_news_link()
        self.should_be_featured_sections_link()
        self.should_be_account_settings_link()
        self.should_be_admin_users_link()
        self.should_be_logout_button()

    def should_be_logo_link(self):
        assert self.is_element_present(*SidebarLocators.LOGO_LINK), "No Logo"

    def should_be_artists_link(self):
        assert self.is_element_present(*SidebarLocators.ARTISTS_LINK), "No Artists link"

    def should_be_users_link(self):
        assert self.is_element_present(*SidebarLocators.USERS_LINK), "No Users link"

    def should_be_news_link(self):
        assert self.is_element_present(*SidebarLocators.NEWS_LINK), "No News link"

    def should_be_featured_sections_link(self):
        assert self.is_element_present(*SidebarLocators.FEATURED_SECTIONS_LINK), "No Featured Sections link"

    def should_be_account_settings_link(self):
        assert self.is_element_present(*SidebarLocators.ACCOUNT_SETTINGS_LINK), "No Account Settings link"

    def should_be_admin_users_link(self):
        assert self.is_element_present(*SidebarLocators.ADMIN_USERS_LINK), "No Admin Users link"

    def should_be_logout_button(self):
        assert self.is_element_present(*SidebarLocators.LOGOUT_BUTTON), "No Logout button"

    def logo_link_navigates_to_artists_page(self):
        logo_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.LOGO_LINK))
        logo_link.click()

    def artists_link_navigates_to_artists_page(self):
        artists_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.ARTISTS_LINK))
        artists_link.click()

    def users_link_navigates_to_users_page(self):
        users_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.USERS_LINK))
        users_link.click()

    def news_link_navigates_to_news_page(self):
        news_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.NEWS_LINK))
        news_link.click()

    def featured_sections_link_navigates_to_featured_sections_page(self):
        featured_sections_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.FEATURED_SECTIONS_LINK))
        featured_sections_link.click()

    def account_settings_link_navigates_to_account_settings_page(self):
        account_settings_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SidebarLocators.ACCOUNT_SETTINGS_LINK))
        account_settings_link.click()

    def admin_users_link_navigates_to_admin_users_page(self):
        try:
            admin_users_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SidebarLocators.ADMIN_USERS_LINK))
            admin_users_link.click()
        except selenium.common.ElementClickInterceptedException:
            pass

    def logout_button_navigates_to_login_page(self):
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SidebarLocators.LOGOUT_BUTTON))
            logout_button.click()
        except selenium.common.ElementClickInterceptedException:
            pass


