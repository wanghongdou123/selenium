from base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切入frame
        self.driver.switch_to.frame('iframeResult')
        # self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        # 切出frame
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id('submitBTN').text)