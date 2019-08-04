from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class DriverOperations:

    def test(self):
        driver = webdriver.Chrome()
        driver.find_element().send_keys()

    def __init__(self, driver):
        if not isinstance(driver, webdriver.Chrome) or isinstance(driver, webdriver.Firefox) or \
                isinstance(driver, webdriver.Safari):
            raise TypeError('webdriver must be an instance of webdriver')
        self.__driver = driver
        self.__check_types = self.__CheckTypes()

    def _get_url(self, url):
        self.__driver.get(url=url)
        return self

    def _get_current_url(self):
        return self.__driver.current_url

    def _close_driver(self):
        self.__driver.close()
        return self

    def _quit_driver(self):
        self.__driver.quit()
        return self

    def _maximize_window(self):
        self.__driver.maximize_window()
        return self

    def _fullscreen_window(self):
        self.__driver.fullscreen_window()
        return self

    def _get_current_window_handle(self):
        return self.__driver.current_window_handle

    def _add_cookie(self, cookies):
        self.__driver.add_cookie(cookie_dict=cookies)
        return self

    def _delete_all_cookies(self):
        self.__driver.delete_all_cookies()
        return self

    def _delete_cookie(self, cookie):
        self.__driver.delete_cookie(name=cookie)
        return self

    def _get_cookie(self, cookie):
        return self.__driver.get_cookie(name=cookie)

    def _get_cookies(self):
        return self.__driver.get_cookies()

    def _get_window_size(self, window_handle='current'):
        return self.__driver.get_window_size(windowHandle=window_handle)

    def _set_window_size(self, width, height, window_handle='current'):
        self.__driver.set_window_size(width=width, height=height, windowHandle=window_handle)
        return self

    def _get_window_position(self, window_handle='current'):
        return self.__driver.get_window_position(windowHandle=window_handle)

    def _set_window_position(self, position_x, position_y, window_handle='current'):
        self.__driver.set_window_position(width=position_x, height=position_y, windowHandle=window_handle)
        return self

    def _implicitly_wait(self, time_in_seconds):
        self.__driver.implicitly_wait(time_to_wait=time_in_seconds)
        return self

    def _set_page_load_timeout(self, time_in_seconds):
        self.__driver.set_page_load_timeout(time_to_wait=time_in_seconds)
        return self

    def _wait_for_element_visible(self, by, locator, timeout_in_seconds):
        WebDriverWait(self.__driver, timeout=timeout_in_seconds).until(
            expected_conditions.presence_of_element_located((by, locator)))

    def click(self, element):
        self.__check_types.check_web_element(element)
        element.click()
        return self

    def set_text(self, element, text):
        self.__check_types.check_web_element(element)
        element.send_keys(text)
        return self

    class __CheckTypes:

        @staticmethod
        def check_web_element(element):
            if not isinstance(element, WebElement):
                raise TypeError('element should be an instance of WebElement')
