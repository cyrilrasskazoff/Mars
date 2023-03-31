import selenium.common
from .base_page import BasePage
from .locators import UsersPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


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
        time.sleep(3)
        ind_filter_results = self.driver.find_elements(*UsersPageLocators.ACC_TYPE_FILTER_RESULTS)
        for result in ind_filter_results[1:]:
            assert result.text == 'Individual' and result.text != 'Entity', "Individual Filter failed"

    def should_filter_by_entity_account_type_work(self):
        account_type_filter = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER).click()
        entity_account_option = self.driver.find_element(*UsersPageLocators.ACCOUNT_TYPE_FILTER_ENTITY).click()
        time.sleep(3)
        entity_filter_results = self.driver.find_elements(*UsersPageLocators.ACC_TYPE_FILTER_RESULTS)
        for result in entity_filter_results[1:]:
            assert result.text == 'Entity' and result.text != 'Individual', "Entity Filter failed"

    def should_filter_by_email_work(self):
        email = "biom@dispostable.com"
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(email)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        time.sleep(3)
        email_filter_results = self.driver.find_elements(*UsersPageLocators.EMAIL_FILTER_RESULTS)
        for result in email_filter_results[1:]:
            assert result.text == email, "Filter by Email failed"

    def should_filter_by_name_work(self):
        name = "Biom"
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(name)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        time.sleep(3)
        name_filter_results = self.driver.find_elements(*UsersPageLocators.NAME_FILTER_RESULTS)
        for result in name_filter_results[1:]:
            assert name in result.text, "Filter by Name failed"

    def should_navigate_user_to_user_details_page(self):
        email = "biom@dispostable.com"
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(email)
        self.driver.find_element(*UsersPageLocators.EMAIL_OR_NAME_FILTER_INPUT).send_keys(Keys.RETURN)
        time.sleep(3)
        for element in self.driver.find_elements(*UsersPageLocators.EMAIL_FILTER_RESULTS)[1:]:
            element.click()

    def should_filter_by_acc_creation_date_work(self):
        # Notice syntax difference when using WebDriverWait and EC (no '*'):
        # date_picker = self.driver.find_element(*UsersPageLocators.DATE_PICKER)
        # date_picker = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UsersPageLocators.DATE_PICKER))
        start_year = '2022' # picking hte start year = 2022 will automatically pick the start date = 09/01/2022
        end_month = 'October'
        end_day = '31'
        date_picker = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UsersPageLocators.DATE_PICKER))
        date_picker.click()
        filter_by_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UsersPageLocators.FILTER_BY_YEAR))
        filter_by_year.click()
        try:
            year_options = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(UsersPageLocators.YEAR_OPTIONS))
            for year_option in year_options:
                if year_option.text == start_year:
                    year_option.click()
        except selenium.common.StaleElementReferenceException:
            pass
        try:
            month_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UsersPageLocators.MONTH_OPTION))
            while month_option.text != f'{end_month} {start_year}':
                next_month_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(UsersPageLocators.NEXT_MONTH_BTN))
                next_month_btn.click()
        except selenium.common.StaleElementReferenceException:
            pass
        try:
            day_options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
                UsersPageLocators.DAY_OPTIONS))
            for day_option in day_options:
                if day_option.text == end_day:
                    day_option.click()
        except selenium.common.StaleElementReferenceException:
            pass

        date_filter_results = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(UsersPageLocators.DATE_FILTER_RESULTS))
        for date_filter_result in date_filter_results[1:]:
            assert date_filter_result.text[0:2] == '09' or date_filter_result.text[0:2] == '10' \
                   and date_filter_result.text[6:] == '2022', 'Filter by account creation date failed'

    def should_filter_by_active_inactive_work(self):
        active_filter = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UsersPageLocators.ACTIVE_FILTER))
        active_filter.click()
        filter_results = WebDriverWait(self.driver, 10).until((EC.visibility_of_all_elements_located(UsersPageLocators.
                                                                                                     TABLE_DATA)))
        active_filter_results = []
        for result in filter_results:
            active_filter_results.append(result.text)
        inactive_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UsersPageLocators.INACTIVE_FILTER))
        inactive_filter.click()
        filter_results = WebDriverWait(self.driver, 10).until((EC.visibility_of_all_elements_located(UsersPageLocators.
                                                                                                     TABLE_DATA)))
        inactive_filter_results = []
        for result in filter_results:
            inactive_filter_results.append(result.text)
        assert active_filter_results != inactive_filter_results, 'Filter by Active/Inactive account type failed'

    def should_pagination_work(self):
        try:
            next_page_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(UsersPageLocators.NEXT_PAGE_BTN))
            btn_disabled = next_page_button.get_attribute("disabled")
            if btn_disabled == "true":
                print('There is only one page')
            else:
                while btn_disabled is None:
                    page_data = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located(UsersPageLocators.TABLE_DATA))
                    page_results = []
                    for data in page_data:
                        page_results.append(data.text)
                    next_page_button.click()
                    try:
                        page_data = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_all_elements_located(UsersPageLocators.TABLE_DATA))
                        new_page_results = []
                        for data in page_data:
                            new_page_results.append(data.text)

                        assert page_results != new_page_results, 'Pagination test failed'
                    except selenium.common.StaleElementReferenceException:
                        pass
        except selenium.common.ElementClickInterceptedException:
            pass

    def should_clear_button_work(self):
        default_data = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(UsersPageLocators.TABLE_DATA))
        default_table_results = []
        for data in default_data:
            default_table_results.append(data.text)
        account_type_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UsersPageLocators.ACCOUNT_TYPE_FILTER))
        account_type_filter.click()
        individual_account_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UsersPageLocators.ACCOUNT_TYPE_FILTER_INDIVIDUAL))
        individual_account_option.click()
        try:
            ind_filter_data = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(UsersPageLocators.TABLE_DATA))
            ind_filter_results = []
            for data in ind_filter_data:
                ind_filter_results.append(data.text)
        except selenium.common.StaleElementReferenceException:
            pass
        try:
            clear_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UsersPageLocators.CLEAR_BUTTON))
            clear_btn.click()
            time.sleep(2)
            clear_data = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(UsersPageLocators.TABLE_DATA))
            clear_table_results = []
            for data in clear_data:
                clear_table_results.append(data.text)
        except selenium.common.StaleElementReferenceException:
            pass
        assert default_table_results == clear_table_results, 'Clear button functionality failed'


