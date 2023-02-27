from .base_pages import BasePage
from .locators import AuthLocators
from .locators import RegLocators
from .locators import ForgetLocators
import time, os

class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.mail = driver.find_element(*AuthLocators.AUTH_TAB_MAIL)
        self.login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.ls = driver.find_element(*AuthLocators.AUTH_TAB_LS)
        self.plh = driver.find_element(*AuthLocators.AUTH_PLH)
        self.plh_text = driver.find_element(*AuthLocators.AUTH_PLH).text
        self.username = driver.find_element(*AuthLocators.AUTH_INPUT_MOBILE)
        self.passw = driver.find_element(*AuthLocators.AUTH_INPUT_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.forgot = driver.find_element(*AuthLocators.AUTH_FORGOT)
        self.to_reg = driver.find_element(*AuthLocators.AUTH_REG)
        self.vk = driver.find_element(*AuthLocators.AUTH_VK)
        self.ok = driver.find_element(*AuthLocators.AUTH_OK)
        self.s_mail = driver.find_element(*AuthLocators.AUTH_MAIL)
        self.GOOGLE = driver.find_element(*AuthLocators.AUTH_GOOGLE)
        self.YANDEX = driver.find_element(*AuthLocators.AUTH_YANDEX)
 #       self.a_error = driver.find_element(*AuthLocators.AUTH_ERR)

    def tab_phone_click(self):
        self.phone.click()

    def tab_mail_click(self):
        self.mail.click()

    def tab_login_click(self):
        self.login.click()

    def tab_ls_click(self):
        self.ls.click()

    def enter_username(self, value):
        self.username.send_keys(value)

    def auth_un_clear(self):
        self.username.clear()

    def enter_password(self, value):
        self.passw.send_keys(value)

    def auth_btn_click(self):
        self.btn.click()

class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=D7NDwXZE_nY"
        driver.get(url)
        self.fname = driver.find_element(*RegLocators.REG_FNAME)
        self.lname = driver.find_element(*RegLocators.REG_LNAME)