from .base_page import BasePage
from .locators import NewsPageLocators


class NewsPage(BasePage):
    def should_be_news_page(self):
        self.should_be_news_page_title()
        self.should_be_news_url()

    def should_be_news_page_title(self):
        assert self.is_element_present(*NewsPageLocators.NEWS_PAGE_TITLE), "This is not a News page"

    def should_be_news_url(self):
        assert "news" in self.driver.current_url, "This is not a News page"