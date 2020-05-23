from base import Base
import time
import pytest

class TestJs(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys("selenium")
        # self.driver.find_element_by_id('su').click()
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/a[last()]').click()
        time.sleep(2)

        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))



    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        time.sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-20'")
        time.sleep(5)


    




