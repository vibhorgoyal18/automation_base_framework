from selenium import webdriver
from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver):
        if not isinstance(driver, webdriver.Chrome) or isinstance(driver, webdriver.Firefox) or \
                isinstance(driver, webdriver.Safari):
            raise TypeError('webdriver must be an instance of webdriver')
        self.__driver = driver

    def _get_element(self, by, using, multiple = False):
        if by and using:
            if not isinstance(by, By):
                raise TypeError('by should be an instance of selenium.webdriver.common.by.By')
            else:
                if multiple:
                    return self.__driver.find_elements(by, using)
                else:
                    return self.__driver.find_element(by, using)
        else:
            raise ValueError('both by and using are required in parameters')
