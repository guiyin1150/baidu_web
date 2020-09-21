from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    #退出元素-是否存在的状态
    exit_link = (By.XPATH,'//a[text()="退出"]')
    def __init__(self,driver:WebDriver):
        self.driver = driver

    #退出元素是否存在的状态
    def get_element_exists(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.exit_link))
        except:
            return False
        else:
            return True
