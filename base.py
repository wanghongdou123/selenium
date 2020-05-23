from selenium import webdriver
import pytest
import os

class Base():
    def setup(self):
        browser =  os.getenv("browser")
        print(browser)
        if browser == "firefox":
            self.driver = webdriver.Firefox()

        elif browser == "headless":
            self.driver = webdriver.PhantomJS()

        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()