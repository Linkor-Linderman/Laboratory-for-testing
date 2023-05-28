from page_objects.element import BasePageElement
from page_objects.locators import MainPageLocators
from page_objects.locators import ResultsPageLocators


class InputNumberElement(BasePageElement):
    """This class gets the input text from the specified locator"""
    locator = 'number'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def fill_number_input(self, data):
        element = self.driver.find_element(*MainPageLocators.NUMBER_INPUT)
        element.send_keys(data)

    def is_title_matches(self, title):
        return title in self.driver.title

    def get_header(self):
        element = self.driver.find_element(*MainPageLocators.HEADER)
        return element.text

    def click_submit_button(self):
        """Triggers the parenthesis_generation"""
        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()


class ResultsPage(BasePage):
    """Results page action methods come here"""
    def get_results(self):
        element = self.driver.find_element(*ResultsPageLocators.RESULT)
        return element.text
