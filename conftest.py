import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from .pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # parser.addoption('--language', action='store', default="en",
    #                  help="Choose language: en, es, fr, ru... etc")


@pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    # language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        print("\nStarting ChromeBrowser")
        options = Options()
        # options.add_experimental_option('prefs', {'intl.accept_languages': language})
        # options.add_argument("--window-size=1440,900")
        # options.add_argument("start-maximized")
        # options.add_argument("headless")
        options.add_argument("start-fullscreen")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        print("\nStarting FirefoxBrowser")
        options_firefox = OptionsFirefox()
        # options_firefox.set_preference("intl.accept_languages", language)
        # options_firefox.add_argument("--window-size=1440,900")
        # options_firefox.add_argument("start-maximized")
        options_firefox.add_argument("headless")
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="function")
def driver_and_admin_login(request):
    browser_name = request.config.getoption("browser_name")
    # language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        print("\nStarting ChromeBrowser")
        options = Options()
        # options.add_experimental_option('prefs', {'intl.accept_languages': language})
        # options.add_argument("--window-size=1440,900")
        options.add_argument("start-fullscreen")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        print("\nStarting FirefoxBrowser")
        options_firefox = OptionsFirefox()
        # options_firefox.set_preference("intl.accept_languages", language)
        # options_firefox.add_argument("--window-size=1440,900")
        # options_firefox.add_argument("start-maximized")
        # options_firefox.add_argument("headless")
        options_firefox.add_argument("start-fullscreen")
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    yield driver
    print("\nquit browser..")
    driver.quit()