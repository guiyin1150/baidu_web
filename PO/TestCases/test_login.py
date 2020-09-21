import unittest
from selenium import webdriver
import ddt
from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.home_page import HomePage
from PO.TestDatas import Global_Datas as GD
from PO.TestDatas import login_datas as lds

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        #访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
    def test_login_success(self):
        LoginPage(self.driver).login(*lds.success)
        self.assertTrue(HomePage(self.driver).get_element_exists())
    def test_unlogin(self):
        LoginPage(self.driver).login(*lds.unlogin)
        self.assertEqual(LoginPage(self.driver).get_msg_from_unlogin(),"此账号没有经过授权，请联系管理员!")

    @ddt.data(*lds.cases)
    def test_login_failed_wrong_format(self,case):
        #步骤#1.登录页面-登录操作 用户名、密码、期望数据
        lp = LoginPage(self.driver)
        lp.login(case["user"],case["passwd"])

        self.assertEqual(lp.get_msg_from_login_form(),case["check"])










