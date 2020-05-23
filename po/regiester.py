from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class Register:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def register(self):
        # send content
        # click element
        sleep(2)
        self.driver.find_element_by_id('corp_name').send_keys('test')
        self.driver.find_element_by_id('manager_name').send_keys('test')
        sleep(5)
        self.driver.quit()
        return True