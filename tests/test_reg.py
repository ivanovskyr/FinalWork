import pytest
import time
from selenium.webdriver.common.by import By
from pages.rt_page import RegPage


# REG_FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
# REG_LNAME = (By.XPATH, '//input[@name="lastName"]')
# REG_REGION = (By.CLASS_NAME, "lastName")
# REG_EMAIL = (By.ID, "address")
# REG_INPUT_PASS = (By.ID, "password")
# REG_INPUT_PASS_CONFIRM = (By.ID, "password-confirm")
# REG_BTN = (By.NAME, "register")


def test_reg_valid(selenium):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    region = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys('Руслан')
    last_name.clear()
    last_name.send_keys('Вельгельм')
    region.clear()
    region.send_keys('Москва г')
    email.clear()
    email.send_keys(page.reg_mail)
    input_pass.clear()
    input_pass.send_keys(page.reg_pass)
    input_pass_confirm.clear()
    input_pass_confirm.send_keys(page.reg_pass)
    btn.click()
    confirm = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text
    assert page.get_relative_link() == page.login_link and confirm == 'Подтверждение email'

def test_empty_field(selenium):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys('')
    last_name.clear()
    last_name.send_keys('')
    email.clear()
    email.send_keys('')
    input_pass.clear()
    input_pass.send_keys('')
    input_pass_confirm.clear()
    input_pass_confirm.send_keys('')
    btn.click()
    confirm = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text
    assert confirm != 'Подтверждение email'

def test_existing_user(selenium):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys('Руслан')
    last_name.clear()
    last_name.send_keys('Ивановский')
    email.clear()
    email.send_keys('put-inmail@mail.ru')
    input_pass.clear()
    input_pass.send_keys('Qw12345678!')
    input_pass_confirm.clear()
    input_pass_confirm.send_keys('Qw12345678!')
    btn.click()
    alert = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2').text
    assert alert == 'Учётная запись уже существует'
fio_29 = 'Р'*29
fio_30 = 'Р'*30
@pytest.mark.parametrize('fst_name, lname, region_mark, email_mark, pass_mark, pass_cmark',
                         [('Иф', 'По', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('Жак', 'Бар', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         (fio_29, fio_29, 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         (fio_30, fio_30, 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!')],
                         ids=['two_letter', 'three_letter', "fio_29", 'fio_30'])
def test_personal_data_positive(selenium, fst_name, lname, region_mark, email_mark, pass_mark, pass_cmark):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    region = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys(fst_name)
    last_name.clear()
    last_name.send_keys(lname)
    region.clear()
    region.send_keys(region_mark)
    email.clear()
    email.send_keys(email_mark)
    input_pass.clear()
    input_pass.send_keys(pass_mark)
    input_pass_confirm.clear()
    input_pass_confirm.send_keys(pass_cmark)
    btn.click()
    confirm = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text
    alert = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2').text
    assert page.get_relative_link() == page.login_link and confirm == 'Подтверждение email' or alert == 'Учётная запись уже существует'
long_fio = 'Р'*31
@pytest.mark.parametrize('fst_name, lname, region_mark, email_mark, pass_mark, pass_cmark',
                         [('', '', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('', 'Иванов', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('Валентин', '', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('Ж', 'Б', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         (long_fio, long_fio, 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('Ruslan', 'Ivanov', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('Руслан5', 'Иванов7', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('!"№;%:?*', '"№;%:?*()', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!'),
                         ('778', '963', 'Москва г', 'mail@mail.ru', 'Qw12345678!', 'Qw12345678!')],
                         ids=['empty_fio', 'empty_fname', 'empty_lname', 'one_letter', 'long_fio',
                              'fio_english', 'cyrilic_digit', 'spec_symbol', 'digit'])
def test_personal_data_negative(selenium, fst_name, lname, region_mark, email_mark, pass_mark, pass_cmark):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    region = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys(fst_name)
    last_name.clear()
    last_name.send_keys(lname)
    region.clear()
    region.send_keys(region_mark)
    email.clear()
    email.send_keys(email_mark)
    input_pass.clear()
    input_pass.send_keys(pass_mark)
    input_pass_confirm.clear()
    input_pass_confirm.send_keys(pass_cmark)
    btn.click()
    confirm = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text
    # name_err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text
    # fam_err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    # email_err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span/text()')
    # pass_err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text
    # pass_c_err = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text
    assert page.get_relative_link() == page.login_link and confirm != 'Подтверждение email'
           # and (name_err == page.fio_err or fam_err == page.fio_err or email_err == page.email_err
           #  or pass_err == page.pass_err or pass_c_err == page.pass_err)

pass_32 = '!"№;QWas' * 32 # 256 символов
pass_33 = '!"№;QWas' * 33 # 264 символа
@pytest.mark.parametrize('email_mark, pass_mark, pass_cmark',
                         [('', 'Qw12345678!', 'Qw12345678!'),
                         ('', '', ''),
                         ('mail@mail.ru', '', 'Qw12345678!'),
                         ('mail@mail.ru', 'Qw12345678!', ''),
                         ('!"№;%:?*', 'Qw12345678!', 'Qw12345678!'),
                         ('Почта@маил.ру', 'Qw12345678!', 'Qw12345678!'),
                         ('0', 'Qw12345678!', 'Qw12345678!'),
                         ('8999555666', 'Qw12345678!', 'Qw12345678!'),
                         ('899955566677', 'Qw12345678!', 'Qw12345678!'),
                         ('+23999555666', 'Qw12345678!', 'Qw12345678!'),
                         ('02', 'Qw12345678!', 'Qw12345678!'),
                         ('103', 'Qw12345678!', 'Qw12345678!'),
                         ('mail@mail.ru', 'Qw12345', 'Qw12345'),
                         ('mail@mail.ru', 'Йц123456!', 'Йц123456!'),
                         ('mail@mail.ru', '!"№;%:?*', '!"№;%:?*'),
                         ('mail@mail.ru', 'СложныйПароль!', 'СложныйПароль!'),
                         ('mail@mail.ru', pass_32, pass_32),
                         ('mail@mail.ru', pass_33, pass_33),
                         ('mail@mail.ru', ' ', ' ')],
                         ids=['empty_mail', 'empty_entry_data', 'empty_pass', 'empty_pass_c', 'mail_spec_symbol',
                              'mail_cyrilic', 'mail_zero', 'mail_10', 'mail_12', 'mail+2', 'mail_02', 'mail_103',
                              'pass_7', 'pass_cyr_digit', 'pass_spec_symbol', 'pass_cyrilic_spec', 'pass_32', 'pass_33',
                              'pass_space'])
def test_entry_data_negative(selenium, email_mark, pass_mark, pass_cmark):
    page = RegPage(selenium)
    page.go_to_reg()
    first_name = page.driver.find_element(By.XPATH, '//input[@name="firstName"]')
    last_name = page.driver.find_element(By.XPATH, '//input[@name="lastName"]')
    region = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    email = page.driver.find_element(By.ID, "address")
    input_pass = page.driver.find_element(By.ID, "password")
    input_pass_confirm = page.driver.find_element(By.ID, "password-confirm")
    btn = page.driver.find_element(By.NAME, "register")
    first_name.clear()
    first_name.send_keys(page.par_fname)
    last_name.clear()
    last_name.send_keys(page.par_lname)
    region.clear()
    region.send_keys(page.par_region)
    email.clear()
    email.send_keys(email_mark)
    input_pass.clear()
    input_pass.send_keys(pass_mark)
    input_pass_confirm.clear()
    input_pass_confirm.send_keys(pass_cmark)
    btn.click()
    confirm = page.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text
    assert page.get_relative_link() == page.login_link and confirm != 'Подтверждение email'