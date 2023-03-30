import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
import time

link = 'https://stage.mars.solbeg.com/admin'
driver.get(link)
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys('testadmin1@test.com')
driver.find_element(By.NAME, "password").send_keys('Testtest1!')
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[text()= "Users"]').click()

# driver.find_element(By.ID, 'mui-component-select-AccountType').click()
# driver.find_element(By.CSS_SELECTOR, "[data-value = 'individual']").click()
# time.sleep(5)
# filter_results = driver.find_elements(By.XPATH, '//div[data-field="accountType"]')
# print(type(filter_results), len(filter_results))
# table = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div')
# cols = int(table.get_attribute("aria-colcount"))
# rows = int(table.get_attribute("aria-rowcount"))

# data_set = driver.find_elements(By.CLASS_NAME, 'MuiDataGrid-cell')
# for data in data_set:
#     print(data.text, end=' ')

# acc_type = driver.find_elements(By.CSS_SELECTOR, '[data-field="accountType"]')
# for data in acc_type[1:]:
#     print(data.text)


#*********************
# date-picker
# start_year = '2022'
# end_month = 'October'
# end_day = '31'
# date_picker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Account Created"]')))
# date_picker.click()
# filter_by_year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="ArrowDropDownIcon"]')))
# filter_by_year.click()
# try:
#     year_options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'PrivatePickersYear-yearButton')))
#     year_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'PrivatePickersYear-yearButton')))
#     for year_option in year_options:
#         if year_option.text == start_year:
#             year_option.click()
# except selenium.common.StaleElementReferenceException:
#     pass
# try:
#     month_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'MuiPickersCalendarHeader-label')))
#     while month_option.text != f'{end_month} 2022':
#         next_month_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Next month"]')))
#         next_month_btn.click()
# except selenium.common.StaleElementReferenceException:
#     pass
# try:
#     day_options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/button')))
#     day_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/button')))
#     for day_option in day_options:
#         if day_option.text == end_day:
#             day_option.click()
# except selenium.common.StaleElementReferenceException:
#     pass
#
# date_filter_results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[data-field="createdAt"]')))
# date_filter_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-field="createdAt"]')))
# for date_filter_result in date_filter_results[1:]:
#     assert date_filter_result.text[0:2] == '09' or date_filter_result.text[0:2] == '10' and date_filter_result.text[6:] == '2023', 'Filter by date failed'
# time.sleep(5)


# individual_accounts = driver.find_elements(By.CSS_SELECTOR, "[title = 'Individual']")
# for account in individual_accounts:
#     assert "Entity" not in account.text, "Individual Filter failed"
# time.sleep(5)
# driver.find_element(By.ID, 'mui-component-select-AccountType').click()
# driver.find_element(By.CSS_SELECTOR, "[data-value = 'entity']").click()
# time.sleep(5)
# entity_accounts = driver.find_elements(By.CSS_SELECTOR, "[title = 'Entity']")
# for account in entity_accounts:
#     assert "Individual" not in account.text, "Entity Filter failed"
# input_name = driver.find_element(By.NAME, "EmailOrName")
# input_name.send_keys("Kirill")
# input_name.send_keys(Keys.RETURN)

# active_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Active"]')))
# active_filter.click()
# filter_results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'MuiDataGrid-cell')))
# active_filter_results = []
# for filter_result in filter_results:
#     active_filter_results.append(filter_result.text)
# inactive_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Inactive"]')))
# inactive_filter.click()
# filter_results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'MuiDataGrid-cell')))
# inactive_filter_results = []
# for filter_result in filter_results:
#     inactive_filter_results.append(filter_result.text)
# assert active_filter_results != inactive_filter_results, 'Active/inactive filter failed'

try:
    pgn_next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Go to next page"]')))
    btn_disabled = pgn_next_btn.get_attribute("disabled")
    if btn_disabled == "true":
        print('There is only one page')
    else:
        while btn_disabled is None:
            page_data = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'MuiDataGrid-cell')))
            page_results = []
            for data in page_data:
                page_results.append(data.text)
            pgn_next_btn.click()
            try:
                page_data = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'MuiDataGrid-cell')))
                new_page_results = []
                for data in page_data:
                    new_page_results.append(data.text)

                assert page_results != new_page_results, 'Pagination test failed'
            except selenium.common.StaleElementReferenceException:
                pass
except selenium.common.ElementClickInterceptedException:
    pass



driver.quit()
