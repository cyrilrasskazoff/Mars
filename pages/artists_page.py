from .base_page import BasePage
from .locators import ArtistsPageLocators


class ArtistsPage(BasePage):
    def should_be_artists_page(self):
        self.should_be_artists_page_title()
        self.should_be_artists_url()

    def should_be_artists_page_title(self):
        assert self.is_element_present(*ArtistsPageLocators.ARTISTS_PAGE_TITLE), "This is not an Artists page"

    def should_be_artists_url(self):
        assert "artists" in self.driver.current_url, "This is not an Artists page"