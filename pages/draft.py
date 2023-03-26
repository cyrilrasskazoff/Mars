from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
import time

link = 'https://stage.mars.solbeg.com/admin'
driver = webdriver.Chrome()
driver.get(link)
driver.find_element(By.NAME, "email").send_keys('testadmin1@test.com')
driver.find_element(By.NAME, "password").send_keys('Testtest1!')
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[text()= "Users"]').click()
time.sleep(5)
# driver.find_element(By.ID, 'mui-component-select-AccountType').click()
# driver.find_element(By.CSS_SELECTOR, "[data-value = 'individual']").click()
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
input_name = driver.find_element(By.NAME, "EmailOrName")
input_name.send_keys("Kirill")
input_name.send_keys(Keys.RETURN)
driver.quit()