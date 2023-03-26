from .base_page import BasePage
from .locators import FeaturedSectionsLocators


class FeaturedSectionsPage(BasePage):
    def should_be_featured_sections_page(self):
        self.should_be_featured_sections_page_title()
        self.should_be_featured_sections_url()

    def should_be_featured_sections_page_title(self):
        assert self.is_element_present(*FeaturedSectionsLocators.F_SECTIONS_PAGE_TITLE), "This is not a Featured " \
                                                                                         "Sections page"

    def should_be_featured_sections_url(self):
        assert "featured-sections" in self.driver.current_url, "This is not a Featured Sections page"