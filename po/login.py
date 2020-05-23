from po.regiester import Register
from selenium.webdriver.remote.webdriver import WebDriver


class Login:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        self.driver.find_element_by_css_selector('.login_registerBar_link').click()

        return Register(self.driver)

