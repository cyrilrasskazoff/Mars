from .pages.login_page import LoginPage
from .pages.artists_page import ArtistsPage


def test_user_should_see_login_form_on_login_page(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.should_be_login_page()


def test_user_can_login_and_go_to_artists_page(driver):
    url = "https://stage.mars.solbeg.com/admin"
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_artists_page()
    artists_page = ArtistsPage(driver, driver.current_url)
    artists_page.should_be_artists_page()


# def test_user_should_see_login_form(driver):
#     driver.get(url)
#     assert browser.find_element(By.CLASS_NAME, "loginForm__PjCel"), f"No 'Login Form' found!"
#
#
# def test_user_should_navigate_to_artists_page_after_login(driver):
#     driver.implicitly_wait(10)
#     driver.get(url)
#     email = browser.find_element(By.NAME, "email")
#     email.send_keys("testadmin1@test.com")
#     password = browser.find_element(By.NAME, "password")
#     password.send_keys("Testtest1!")
#     submit = browser.find_element(By.TAG_NAME, "button")
#     submit.click()
#     artists = browser.find_element(By.CLASS_NAME, "title__CdGbY")
#     assert "Artists" == artists.text and "artists" in browser.current_url, "Login failed or Login redirected to the " \
#                                                                            "wrong page "
#     # time.sleep(5)
#     # assert "artists" in browser.current_url, "Login failed or Login redirected to the wrong page"



# the default browser is Chrome
# to use Firefox use: pytest -s -v --browser_name=firefox test_login_page.py

