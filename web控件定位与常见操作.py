import pytest
from selenium import webdriver
from time import sleep

class TestWait():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def teardown(self):
        self.driver.quit()


    def test_openbaidu(self):
        sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("测试")
        # self.driver.find_element_by_css_selector('#kw').send_keys("测试")
        self.driver.find_element_by_css_selector('[id=kw]').send_keys("测试")
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)

