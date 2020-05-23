# 直接等待
# 强制等待，线程休眠一定的时间
# time.sleep(3)

# 隐式等待
# 设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没出现就抛出异常
# 全局设置，作用于所有的findelement
# 确定：A可能需要等待100，B只需要等待1
# self.driver.implicitly_wait(3)

# 显式等待
# 在代码中有定义等待条件，当条件发生时才执行代码
# 程序每隔0.5秒轮询进行条件判断，如果条件成立，则执行下一步，否则继续等待，知道超过设置的时间

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.maximize_window()
        # 3、隐式等待
        # self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.find_element_by_xpath('//*[@title="归入各种类别的所有主题"]').click()
        # # 1、强制等待
        # time.sleep(3)

        # # 2、显式等待
        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath('//*[@class="table-heading"]')) >= 1
        # WebDriverWait(self.driver,10).until(wait)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))

        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()










