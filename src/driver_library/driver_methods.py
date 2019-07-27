from selenium import webdriver


class DriverMethods:

    # def test(self):
    #     driverTest = webdriver.Chrome()
    #     driverTest.maximize_window()

    def __init__(self, driver):
        if not isinstance(driver, webdriver.Chrome) or isinstance(driver, webdriver.Firefox) or \
                isinstance(driver, webdriver.Safari):
            raise TypeError('webdriver must be an instance of webdriver')

        self.driver = driver

    def _get_url(self, url):
        self.driver.get(url)
        return self

    def _close_driver(self):
        self.driver.close()
        return self

    def _quit_driver(self):
        self.driver.quit()
        return self

    def _maximize_window(self):
        self.driver.maximize_window()
        return self
