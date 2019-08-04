from src.driver_library.driver_initializer import Browser, DriverInitializer
from src.driver_library.driver_methods import DriverOperations
from src.driver_library.web_element import WebElement
from selenium.webdriver.common.by import By


class Test(DriverOperations, WebElement):

    def __init__(self):
        driver = DriverInitializer().get_driver(Browser.CHROME)
        DriverOperations.__init__(self, driver)
        WebElement.__init__(self, driver)
        super()._implicitly_wait(10)._get_url('https://www.google.com/')

        element = super()._get_element(By.NAME, 'q')
        super().set_text(element, 'search')
        super()._quit_driver()


test = Test()
