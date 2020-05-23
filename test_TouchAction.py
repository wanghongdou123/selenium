import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()


    @pytest.mark.skip
    def test_touchaction(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele.send_keys('selenium测试')
        action = TouchActions(self.driver)
        ele_search = self.driver.find_element_by_id('su')
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele_search,0,10000).perform()

    # form
    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys('Alieen617')
        self.driver.find_element_by_id('user_password').send_keys('whd19931121')
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_xpath('//*[@type="submit"]').click()
        sleep(3)
