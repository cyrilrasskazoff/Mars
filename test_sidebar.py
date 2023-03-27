from .pages.sidebar import Sidebar
from .pages.news_page import NewsPage
from .pages.users_page import UsersPage
from .pages.featured_sections_page import FeaturedSectionsPage
from .pages.admin_users_page import AdminUsersPage
from .pages.account_settings import AccountSettingsPage
from .pages.login_page import LoginPage
from .pages.artists_page import ArtistsPage


def test_admin_user_should_see_sidebar_menu_after_login(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.should_be_sidebar_menu()


def test_admin_user_is_navigated_to_users_page_after_clicking_on_users_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()


def test_admin_user_is_navigated_to_news_page_after_clicking_on_news_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.news_link_navigates_to_news_page()
    news_page = NewsPage(driver, url)
    news_page.should_be_news_page()


def test_admin_user_is_navigated_to_artists_page_after_clicking_on_artists_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.artists_link_navigates_to_artists_page()
    artists_page = ArtistsPage(driver, url)
    artists_page.should_be_artists_page()


def test_admin_user_is_navigated_to_featured_sections_page_after_clicking_on_featured_sections_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.featured_sections_link_navigates_to_featured_sections_page()
    f_sections_page = FeaturedSectionsPage(driver, url)
    f_sections_page.should_be_featured_sections_page()


def test_admin_user_is_navigated_to_artists_page_after_clicking_on_logo_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.logo_link_navigates_to_artists_page()
    artists_page = ArtistsPage(driver, url)
    artists_page.should_be_artists_page()


def test_admin_user_is_navigated_to_admin_user_page_after_clicking_on_admin_users_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.admin_users_link_navigates_to_admin_users_page()
    admin_users_page = AdminUsersPage(driver, url)
    admin_users_page.should_be_admin_users_page()


def test_admin_user_is_navigated_to_account_settings_page_after_clicking_on_account_settings_link(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.account_settings_link_navigates_to_account_settings_page()
    acc_settings_page = AccountSettingsPage(driver, url)
    acc_settings_page.should_be_account_settings_page()


def test_admin_user_is_navigated_to_login_page_after_clicking_on_logout_btn(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.logout_button_navigates_to_login_page()
    login_page = LoginPage(driver, url)
    login_page.should_be_login_page()