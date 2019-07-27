from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum

class DriverInitializer:

    def get_driver(self, browser):
        if not isinstance(browser, Browser):
            raise TypeError('browser must be an instance of Browser Enum')

        if browser is Browser.CHROME:
            return self.__get_chrome_driver()

        elif browser is Browser.HEADLESS_CHROME:
            return self.__get_chrome_headless_driver()

        elif browser is Browser.FIREFOX:
            return self.__get_firefox_driver()

        elif browser is Browser.SAFARI:
            return self.__get_safari_driver()

    @staticmethod
    def __get_chrome_driver():
        return webdriver.Chrome()

    @staticmethod
    def __get_chrome_headless_driver():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        return webdriver.Chrome(chrome_options)

    @staticmethod
    def __get_firefox_driver():
        return webdriver.Firefox()

    @staticmethod
    def __get_safari_driver():
        return webdriver.Safari()


class Browser(Enum):
    CHROME = 1
    HEADLESS_CHROME = 2
    FIREFOX = 3
    SAFARI = 4
