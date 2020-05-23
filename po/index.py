from po.login import Login
from po.regiester import Register
from selenium import webdriver
from time import sleep


class Index:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        # click login
        sleep(2)
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return Login(self.driver)

    def goto_register(self):
        # click register
        sleep(2)
        self.driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)