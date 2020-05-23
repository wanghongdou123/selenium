from base import Base

class TestWindows(Base):

    def test_window(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('18401504837')
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_xpath('//*[@title="用户名登录"]').click()
        self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('login_name')
        self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('login_password')
        self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()












