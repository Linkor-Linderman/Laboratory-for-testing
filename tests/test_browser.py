import pytest
import page_objects.page as page

BASE_URL = 'http://localhost:5000/'


class TestParenthesisUi:
    def test_check_parenthesis_array_with_correct_number(self, browser):
        browser.get(BASE_URL)
        main_page = page.MainPage(browser)
        main_page.fill_number_input(1)
        main_page.click_submit_button()
        search_results_page = page.ResultsPage(browser)
        expected = ' '.join(str(x) for x in ["()"])
        assert search_results_page.get_results() == expected

    def test_main_page_opens_with_expected_title(self, browser):
        browser.get(BASE_URL)
        main_page = page.MainPage(browser)
        assert main_page.is_title_matches("This is Test App Title"), "Title doesn't match."

    def test_main_page_opens_with_expected_header(self, browser):
        browser.get(BASE_URL)
        main_page = page.MainPage(browser)
        assert main_page.get_header() == "This is Test App Header", "Header doesn't match."

    def test_check_parenthesis_array_with_incorrect_number(self, browser):
        browser.get(BASE_URL)
        main_page = page.MainPage(browser)
        main_page.fill_number_input(9)
        main_page.click_submit_button()
        assert main_page.is_title_matches("400 Bad Request")

    def test_check_parenthesis_array_with_empty_input(self, browser):
        browser.get(BASE_URL)
        main_page = page.MainPage(browser)
        main_page.fill_number_input('')
        main_page.click_submit_button()
        assert main_page.is_title_matches("400 Bad Request")
