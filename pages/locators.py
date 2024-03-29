from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_TAB_MAIL = (By.ID, "t-btn-tab-mail")
    AUTH_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_TAB_LS = (By.ID, "t-btn-tab-ls")
    AUTH_PLH = (By.CLASS_NAME, "rt-input__placeholder")
    AUTH_INPUT_MOBILE = (By.ID, "username")
    AUTH_INPUT_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_FORGOT = (By.ID, "forgot_password")
    AUTH_REG = (By.ID, "kc-register")
    AUTH_VK = (By.ID, "oidc_vk")
    AUTH_OK = (By.ID, "oidc_ok")
    AUTH_MAIL = (By.ID, "oidc_mail")
    AUTH_GOOGLE = (By.ID, "oidc_google")
    AUTH_YANDEX = (By.ID, "oidc_ya")

class RegLocators:
     TO_REG = (By.ID, "kc-register")

class ForgetLocators:
    FORGET_BTN = (By.NAME, 'reset')
    CAPCHA = (By.ID, 'captcha')

