from .pages.sidebar import Sidebar
from .pages.users_page import UsersPage
from .pages.login_page import LoginPage
from .pages.user_details_page import UserDetailsPage
url = "https://stage.mars.solbeg.com/admin"


def test_admin_is_redirected_to_users_page_after_successful_login_and_onclick_users_link_in_sidebar(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()


def test_filter_by_individual_account_type_should_work(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_individual_account_type_work()


def test_filter_by_entity_account_type_should_work(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_entity_account_type_work()


def test_search_by_email(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_email_work()


def test_search_by_name(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_name_work()


def test_admin_is_navigated_to_user_details_page_after_onclick_user(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_navigate_user_to_user_details_page()
    user_details_page = UserDetailsPage(driver_and_admin_login, url)
    user_details_page.should_be_user_details_page()


def test_filter_by_account_creation_date_should_work(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_acc_creation_date_work()


def test_filter_by_active_inactive_acc_type_should_work(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_filter_by_active_inactive_work()


def test_pagination_on_users_page_should_work(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_pagination_work()


def test_clear_button_should_clear_applied_filters_and_display_default_page_data(driver_and_admin_login):
    page = Sidebar(driver_and_admin_login, url)
    page.users_link_navigates_to_users_page()
    users_page = UsersPage(driver_and_admin_login, url)
    users_page.should_be_users_page()
    users_page.should_clear_button_work()

