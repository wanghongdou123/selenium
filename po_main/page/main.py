from selenium.webdriver.common.by import By

from po_main.page.add_member import AddMember
from po_main.page.base_page import BasePage


class Main(BasePage):

    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # click add member
        self.find(By.ID, 'menu_contacts').click()
        # 显式等待10秒
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        self.wait_for_click(locator)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self.driver)
