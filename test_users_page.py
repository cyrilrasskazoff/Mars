from .pages.sidebar import Sidebar
from .pages.users_page import UsersPage
from .pages.login_page import LoginPage
from .pages.user_details_page import UserDetailsPage
url = "https://stage.mars.solbeg.com/admin"


def test_admin_is_redirected_to_users_page_after_successful_login_and_onclick_users_link_in_sidebar(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()


def test_filter_by_individual_account_type_should_work(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_individual_account_type_work()


def test_filter_by_entity_account_type_should_work(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_entity_account_type_work()


def test_search_by_email(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_email_work()


def test_search_by_name(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_name_work()


def test_admin_is_navigated_to_user_details_page_after_onclick_user(driver):
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    page = Sidebar(driver, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver, url)
    users_page.should_be_users_page()
    users_page.should_navigate_user_to_user_details_page()
    user_details_page = UserDetailsPage(driver, url)
    user_details_page.should_be_user_details_page()

