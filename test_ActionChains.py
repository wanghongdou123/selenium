import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()


    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #  //input[@value="click me"]
        element_click = self.driver.find_element_by_xpath('//*[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//*[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//*[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()


    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath('//*[@class="item"][1]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()


    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('//label[1]/input[@type="textbox"]')
        action = ActionChains(self.driver)
        action.send_keys("username")
        action.send_keys(Keys.SPACE)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()


if __name__ == '__main__':
    pytest.main('-v','-s','test_ActionChains.py')



