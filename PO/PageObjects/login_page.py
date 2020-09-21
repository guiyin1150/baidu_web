from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.login_page_locs import LoginPageLocs as loc
class  LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def login(self,username,passwd):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.login_button))
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.passwd_input).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()

    #获取登录区域的提示信息
    def get_msg_from_login_form(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.msg_from_login_form))
        eles = self.driver.find_elements(*loc.msg_from_login_form)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for el in eles:
                text_list.append(el.text)
            return text_list
    #获取未注册的信息
    def get_msg_from_unlogin(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.msg_from_unlogin))
        element = self.driver.find_element(*loc.msg_from_unlogin).text
        return element

