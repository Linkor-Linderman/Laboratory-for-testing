from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SUBMIT_BUTTON = (By.ID, 'submit')
    NUMBER_INPUT = (By.ID, 'number')
    HEADER = (By.TAG_NAME, 'h1')


class ResultsPageLocators(object):
    """A class for results locators. All results locators should come here"""
    RESULT = (By.ID, 'result')
