from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "loginForm__PjCel")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")


class ArtistsPageLocators:
    # ARTISTS_PAGE_TITLE = (By.CLASS_NAME, "title__CdGbY")
    ARTISTS_PAGE_TITLE = (By.XPATH, '//h1[text()="Artists"]')


class SidebarLocators:
    LOGO_LINK = (By.XPATH, '//a[@href= "/admin"]')
    ARTISTS_LINK = (By.XPATH, '//span[text()= "Artists"]')
    USERS_LINK = (By.XPATH, '//span[text()= "Users"]')
    NEWS_LINK = (By.XPATH, '//span[text()= "News"]')
    FEATURED_SECTIONS_LINK = (By.XPATH, '//span[text()= "Featured Sections"]')
    ACCOUNT_SETTINGS_LINK = (By.XPATH, '//span[text()= "Account Settings"]')
    ADMIN_USERS_LINK = (By.XPATH, '//span[text()= "Admin Users"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Log Out"]')


class UsersPageLocators:
    USERS_PAGE_TITLE = (By.XPATH, '//h1[text()="Users"]')
    ACCOUNT_TYPE_FILTER = (By.ID, 'mui-component-select-AccountType')
    ACCOUNT_TYPE_FILTER_INDIVIDUAL = (By.CSS_SELECTOR, "[data-value = 'individual']")
    ACCOUNT_TYPE_FILTER_ENTITY = (By.CSS_SELECTOR, "[data-value = 'entity']")
    ACC_TYPE_FILTER_RESULTS = (By.CSS_SELECTOR, '[data-field="accountType"]')
    EMAIL_OR_NAME_FILTER_INPUT = (By.NAME, "EmailOrName")
    EMAIL_FILTER_RESULTS = (By.CSS_SELECTOR, '[data-field="email"]')
    # EMAIL_FILTER_RESULT = (By.CSS_SELECTOR, f'[title = "{email}"]')
    NAME_FILTER_RESULTS = (By.CSS_SELECTOR, '[data-field="name"]')
    TABLE_DATA = (By.CLASS_NAME, 'MuiDataGrid-cell')
    DATE_PICKER = (By.CSS_SELECTOR, '[placeholder="Account Created"]')
    FILTER_BY_YEAR = (By.CSS_SELECTOR, '[data-testid="ArrowDropDownIcon"]')
    YEAR_OPTIONS = (By.CLASS_NAME, 'PrivatePickersYear-yearButton')
    YEAR_OPTION = (By.CLASS_NAME, 'PrivatePickersYear-yearButton')
    MONTH_OPTION = (By.CLASS_NAME, 'MuiPickersCalendarHeader-label')
    NEXT_MONTH_BTN = (By.CSS_SELECTOR, '[title="Next month"]')
    DAY_OPTIONS = (By.XPATH, '//html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/button')
    DAY_OPTION = (By.XPATH, '//html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/button')
    DATE_FILTER_RESULTS = (By.CSS_SELECTOR, '[data-field="createdAt"]')
    DATE_FILTER_RESULT = (By.CSS_SELECTOR, '[data-field="createdAt"]')


class UserDetailsPageLocators:
    MANAGE_USER_BUTTON = (By.XPATH, "//button[text() = 'manage User']")


class NewsPageLocators:
    NEWS_PAGE_TITLE = (By.XPATH, '//div[text()="News"]')


class FeaturedSectionsLocators:
    F_SECTIONS_PAGE_TITLE = (By.XPATH, '//div[text()="Featured Sections"]')


class AccountSettingsLocators:
    ACCOUNT_SETTINGS_PAGE_TITLE = (By.XPATH, '//div[text()="Account Settings"]')


class AdminUsersLocators:
    ADMIN_USERS_PAGE_TITLE = (By.XPATH, '//div[text()="Admin Users"]')


