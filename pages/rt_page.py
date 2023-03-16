from .base_pages import BasePage
from .locators import AuthLocators
from .locators import RegLocators
import os

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
        self.username = driver.find_element(*AuthLocators.AUTH_INPUT_MOBILE)
        self.passw = driver.find_element(*AuthLocators.AUTH_INPUT_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.forgot = driver.find_element(*AuthLocators.AUTH_FORGOT)
        self.to_reg = driver.find_element(*AuthLocators.AUTH_REG)
        self.vk = driver.find_element(*AuthLocators.AUTH_VK)
        self.auth_vk = '/authorize'
        self.ok = driver.find_element(*AuthLocators.AUTH_OK)
        self.auth_ok = '/dk'
        self.s_mail = driver.find_element(*AuthLocators.AUTH_MAIL)
        self.auth_mail = '/oauth/authorize'
        self.GOOGLE = driver.find_element(*AuthLocators.AUTH_GOOGLE)
        self.auth_google = '/o/oauth2/auth/oauthchooseaccount'
        self.YANDEX = driver.find_element(*AuthLocators.AUTH_YANDEX)
        self.auth_ya = '/auth'
        self.auth_link = '/auth/realms/b2c/protocol/openid-connect/auth'
        self.success_auth_link = '/account_b2c/page'
        self.reg_link = '/auth/realms/b2c/login-actions/registration'
        self.forgot_link = '/auth/realms/b2c/login-actions/reset-credentials'
        self.act_mail = 'put-inmail@mail.ru'
        self.act_pass = 'Qw12345678!'


    def tab_phone_click(self):
        self.phone.click()

    def tab_mail_click(self):
        self.mail.click()

    def tab_login_click(self):
        self.login.click()

    def tab_ls_click(self):
        self.ls.click()

    def enter_username(self, value):
        self.username.clear()
        self.username.send_keys(value)

    def enter_password(self, value):
        self.passw.clear()
        self.passw.send_keys(value)

    def auth_btn_click(self):
        self.btn.click()

    def auth_pass_click(self):
        self.passw.click()

class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.to_reg = driver.find_element(*RegLocators.TO_REG)
        self.reg_mail = 'ivryslan1@gmail.com'
        self.reg_pass = 'Qw12345678!'
        self.login_link = '/auth/realms/b2c/login-actions/registration'
        self.fio_err = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        self.email_err = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        self.pass_err = 'Длина пароля должна быть не менее 8 символов'
        self.par_region = 'Москва г'
        self.par_fname = 'Виктор'
        self.par_lname = 'Иванов'

    def go_to_reg(self):
        self.to_reg.click()

class ForgotPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.to_forgot = driver.find_element(*AuthLocators.AUTH_FORGOT)
        self.phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.mail = driver.find_element(*AuthLocators.AUTH_TAB_MAIL)
        self.login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.ls = driver.find_element(*AuthLocators.AUTH_TAB_LS)
        self.plh = driver.find_element(*AuthLocators.AUTH_PLH)
        self.username = driver.find_element(*AuthLocators.AUTH_INPUT_MOBILE)
        self.auth_link = '/auth/realms/b2c/login-actions/authenticate'
        self.recovery_text = 'Код подтверждения отправлен на адрес p*********@mail.ru'
        self.valid_mail = 'put-inmail@mail.ru'