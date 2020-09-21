from selenium.webdriver.common.by import By
class LoginPageLocs:

    #用户名输入框
    user_input = (By.XPATH,'//input[@name="phone"]')
    #密码输入框
    passwd_input = (By.XPATH,'//input[@name="password"]')
    #登录按钮
    login_button = (By.TAG_NAME, 'button')
    # 登陆表单区域的提示信息框
    msg_from_login_form = (By.XPATH,'//div[@class="form-error-info"]')
    #未注册手机号的提示框
    msg_from_unlogin = (By.XPATH,'//div[@class="layui-layer-content"]')