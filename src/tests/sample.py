from src.driver_library.driver_initializer import Browser, DriverInitializer
from src.driver_library.driver_methods import DriverMethods


class Test(DriverMethods):
    driver = DriverInitializer().get_driver(Browser.CHROME)
    driver_methods = DriverMethods(driver)
    driver_methods._get_url('https://www.google.com/')._close_driver()
