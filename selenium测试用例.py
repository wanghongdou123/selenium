# 1. 打开页面"https://testerhome.com"
# 2. 点击-社团 标签
# 3. 点击-霍格沃兹学员
# 4. 访问顶部的第一个帖子


from selenium import webdriver
# from time import sleep

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_xpath("//*[@id='hot_teams']/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
        self.driver.find_element_by_css_selector(".topic-22287 .title > a").click()



