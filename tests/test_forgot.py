import pytest
import time
from selenium.webdriver.common.by import By
from pages.rt_page import ForgotPage

# При выборе таба плэйсхолдер меняется на соответствующий
def test_phone_tab(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    mail = page.driver.find_element(By.ID, "t-btn-tab-mail") # Для начала переходим на вкладку Почта, чтобы проверить обратный переход
    phone = page.driver.find_element(By.ID, "t-btn-tab-phone")
    mail.click()
    phone.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Мобильный телефон"
def test_mail_tab(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    mail = page.driver.find_element(By.ID, "t-btn-tab-mail")
    mail.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Электронная почта"
def test_login_tab(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    login = page.driver.find_element(By.ID, "t-btn-tab-login")
    login.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Логин"
def test_ls_tab(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    ls = page.driver.find_element(By.ID, "t-btn-tab-ls")
    ls.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Лицевой счёт"

# При вводе в поле username номера телефона плэйсхолдер становится "Мобильный телефон".
# Предварительно переходим на таб "Электронная почта"
def test_change_placeholder_phone(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    mail = page.driver.find_element(By.ID, "t-btn-tab-mail")
    mail.click() # Для начала переходим на вкладку Почта, чтобы проверить обратный переход
    username = page.driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("89998885533")
    captha.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Мобильный телефон"
# При вводе в поле username электронной почты плэйсхолдер становится "Электронная почта"
def test_change_placeholder_mail(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("mail@mail.ru")
    captha.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Электронная почта"
# При вводе в поле username логина плэйсхолдер становится "Логин"
def test_change_placeholder_login(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("alex")
    captha.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Логин"
# При вводе в поле username лицевого счета плэйсхолдер становится "Лицевой счет"
def test_change_placeholder_ls(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("123456789123")
    captha.click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Лицевой счёт"

def test_recovery_empty_phone(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    phone = page.driver.find_element(By.ID, "t-btn-tab-phone")
    fgt_btn = page.driver.find_element(By.NAME, 'reset')
    phone.click()
    username.clear()
    captha.click()
    time.sleep(10)
    fgt_btn.click()
    err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert err == "Введите номер телефона"

def test_recovery_empty_mail(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    mail = page.driver.find_element(By.ID, "t-btn-tab-mail")
    fgt_btn = page.driver.find_element(By.NAME, 'reset')
    mail.click()
    username.clear()
    captha.click()
    time.sleep(10)
    fgt_btn.click()
    err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert err == "Введите адрес, указанный при регистрации"

def test_recovery_empty_login(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    login = page.driver.find_element(By.ID, "t-btn-tab-login")
    fgt_btn = page.driver.find_element(By.NAME, 'reset')
    login.click()
    username.clear()
    captha.click()
    time.sleep(10)
    fgt_btn.click()
    err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert err == "Введите логин, указанный при регистрации"

def test_recovery_empty_ls(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    ls = page.driver.find_element(By.ID, "t-btn-tab-ls")
    fgt_btn = page.driver.find_element(By.NAME, 'reset')
    ls.click()
    username.clear()
    captha.click()
    time.sleep(10)
    fgt_btn.click()
    err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert err == "Введите номер вашего лицевого счета"

def test_btn_back(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    reset_back = page.driver.find_element(By.ID, 'reset-back')
    reset_back.click()
    assert page.get_relative_link() == page.auth_link

def test_recovery_mail(selenium):
    page = ForgotPage(selenium)
    page.to_forgot.click()
    captha = page.driver.find_element(By.ID, 'captcha')
    username = page.driver.find_element(By.ID, "username")
    mail = page.driver.find_element(By.ID, "t-btn-tab-mail")
    fgt_btn = page.driver.find_element(By.NAME, 'reset')
    mail.click()
    username.clear()
    username.send_keys(page.valid_mail)
    captha.click()
    time.sleep(10)
    fgt_btn.click()
    message = page.driver.find_element(By.CLASS_NAME, 'card-container__desc').text
    assert message == page.recovery_text