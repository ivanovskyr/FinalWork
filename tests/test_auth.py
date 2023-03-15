import pytest
import time
from selenium.webdriver.common.by import By
from pages.rt_page import AuthPage

# При выборе таба плэйсхолдер меняется на соответствующий
def test_phone_tab(selenium):
    page = AuthPage(selenium)
    page.tab_phone_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Мобильный телефон"
def test_mail_tab(selenium):
    page = AuthPage(selenium)
    page.tab_mail_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Электронная почта"
def test_login_tab(selenium):
    page = AuthPage(selenium)
    page.tab_login_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Логин"
def test_ls_tab(selenium):
    page = AuthPage(selenium)
    page.tab_ls_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Лицевой счёт"

# При вводе в поле username номера телефона плэйсхолдер становится "Мобильный телефон".
# Предварительно переходим на таб "Электронная почта"
def test_change_placeholder_phone(selenium):
    page = AuthPage(selenium)
    page.tab_mail_click()
    page.enter_username("89998885533")
    page.auth_pass_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Мобильный телефон"
# При вводе в поле username электронной почты плэйсхолдер становится "Электронная почта"
def test_change_placeholder_mail(selenium):
    page = AuthPage(selenium)
    page.enter_username("yandex@yandex.ru")
    page.auth_pass_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Электронная почта"
# При вводе в поле username логина плэйсхолдер становится "Логин"
def test_change_placeholder_login(selenium):
    page = AuthPage(selenium)
    page.enter_username("alex")
    page.auth_pass_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Логин"
# При вводе в поле username лицевого счета плэйсхолдер становится "Лицевой счет"
def test_change_placeholder_ls(selenium):
    page = AuthPage(selenium)
    page.enter_username('895654221456')
    page.auth_pass_click()
    plh = page.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
    assert plh == "Лицевой счёт"
#
def test_empry_phone_field(selenium):
    page = AuthPage(selenium)
    page.tab_phone_click()
    page.enter_username('')
    page.enter_password('')
    page.auth_btn_click()
    err_text = page.driver.find_element(By.CSS_SELECTOR,
                                        (".rt-input-container__meta.rt-input-container__meta--error")).text
    assert err_text == "Введите номер телефона"
def test_emptu_mail_field(selenium):
    page = AuthPage(selenium)
    page.tab_mail_click()
    page.enter_username('')
    page.enter_password('')
    page.auth_btn_click()
    err_text = page.driver.find_element(By.CSS_SELECTOR,
                                        (".rt-input-container__meta.rt-input-container__meta--error")).text
    assert err_text == "Введите адрес, указанный при регистрации"
def test_emptu_login_field(selenium):
    page = AuthPage(selenium)
    page.tab_login_click()
    page.enter_username('')
    page.enter_password('')
    page.auth_btn_click()
    err_text = page.driver.find_element(By.CSS_SELECTOR,
                                        (".rt-input-container__meta.rt-input-container__meta--error")).text
    assert err_text == "Введите логин, указанный при регистрации"
def test_emptu_ls_field(selenium):
    page = AuthPage(selenium)
    page.tab_ls_click()
    page.enter_username('')
    page.enter_password('')
    page.auth_btn_click()
    err_text = page.driver.find_element(By.CSS_SELECTOR,
                                        (".rt-input-container__meta.rt-input-container__meta--error")).text
    assert err_text == "Введите номер вашего лицевого счета"
# Авторизация с валидными почтой и паролем
def test_auth_valid_mail_pass(selenium):
    page = AuthPage(selenium)
    page.enter_username(page.act_mail)
    page.enter_password(page.act_pass)
    page.auth_btn_click()
    assert page.get_relative_link() == page.success_auth_link

# Переход на форму регистрации
def test_auth_to_reg(selenium):
    page = AuthPage(selenium)
    page.to_reg.click()
    assert page.get_relative_link() == page.reg_link
# Переход на форму восстановления пароля
def test_auth_to_forgot(selenium):
    page = AuthPage(selenium)
    page.forgot.click()
    assert page.get_relative_link() == page.forgot_link

@pytest.mark.parametrize('user_name, password, expected', [('89995556622', '857496321!Df', 'Неверный логин или пароль'),
                                                           ('mail@mail.ru', '857496321!Df', 'Неверный логин или пароль'),
                                                           ('alex', '857496321!Df', 'Неверный логин или пароль'),
                                                           ('495654221456', '857496321!Df', 'Неверный логин или пароль'),
                                                           ('ivryslan@gmail.com', '857496321!Df', 'Неверный логин или пароль')],
                         ids=['mobile_pass_invalid', 'mail_pass_invalid', 'login_pass_invalid', 'ls_pass_invalid', 'mail_valid_pass_invalid'])
def test_no_valid(selenium, user_name, password, expected):
    page = AuthPage(selenium)
    page.enter_username(user_name)
    page.enter_password(password)
    time.sleep(8)
    page.auth_btn_click()
    err_text = page.driver.find_element(By.ID, 'form-error-message').text
    assert page.get_relative_link() != page.reg_link and err_text == expected
# Авторизация с валидной почтой и пустым паролем
def test_valid_mail_empty_pass(selenium):
    page = AuthPage(selenium)
    page.enter_username('ivryslan@gmail.com')
    page.enter_password('')
    time.sleep(8)
    page.auth_btn_click()
    assert page.get_relative_link() != page.reg_link
# Авторизация с невалидным полем номера телефона/почты/логина/лицевого счета и валидным паролем
@pytest.mark.parametrize('user_name, password',
                         [('89995556622', 'Qw12345678!'),
                          ('mail@mail.ru', 'Qw12345678!'),
                          ('alex', 'Qw12345678!'),
                          ('495654221456', 'Qw12345678!')],
                         ids=['invalid_phone_valid_pass', 'invalid_mail_valid_pass',
                              'invalid_login_valid_pass', 'invalid_ls_valid_pass'])
def test_empty_username_valid_pass(selenium, user_name, password):
    page = AuthPage(selenium)
    page.enter_username(user_name)
    page.enter_password(password)
    time.sleep(10)
    page.auth_btn_click()
    err_text = page.driver.find_element(By.ID, 'form-error-message').text
    assert page.get_relative_link() != page.reg_link and err_text == 'Неверный логин или пароль'

def test_social_link_vk(selenium):
    page = AuthPage(selenium)
    page.vk.click()
    assert page.get_relative_link() == page.auth_vk

def test_social_link_ok(selenium):
    page = AuthPage(selenium)
    page.ok.click()
    assert page.get_relative_link() == page.auth_ok

def test_social_link_mail(selenium):
    page = AuthPage(selenium)
    page.s_mail.click()
    assert page.get_relative_link() == page.auth_mail

def test_social_link_google(selenium):
    page = AuthPage(selenium)
    page.GOOGLE.click()
    assert page.get_relative_link() == page.auth_google

def test_social_link_yandex(selenium):
    page = AuthPage(selenium)
    page.YANDEX.click()
    assert page.get_relative_link() == page.auth_ya