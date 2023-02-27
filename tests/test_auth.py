import pytest

from pages.rt_page import AuthPage
import time
#@pytest.fixture (ids=['Placeholder mobile', 'Placeholder email', 'Placeholder login', 'Placeholder LS'])
@pytest.fixture (scope="function", param=[('89998885533', 'yandex@yandex.ru')], ids=['Placeholder mobile', 'Placeholder email'])
def test_auth(selenium):
    page = AuthPage(selenium)
    page.tab_phone_click()
    page.enter_username("89998885533")
    plh = page.plh_text
    assert plh == "Мобильный телефон"
    page.tab_mail_click()
    page.enter_username("yandex@yandex.ru")
    plh = page.plh_text
    assert plh == "Электронная почта"
    page.tab_login_click()
    page.enter_username("alex")
    plh = page.plh_text
    assert plh == "Логин"
    page.tab_ls_click()
    page.enter_username("895654221456")
    plh = page.plh_text
    assert plh == "Лицевой счёт"
    # page.auth_un_clear()
    # page.enter_password("")
    # page.auth_btn_click()
    #
    # page.tab_mail_click()
    # page.enter_username("")
    # page.enter_password("")
    # page.auth_btn_click()

    # page.tab_ls_click()
    # assert
    # time.sleep(1)
    # page.tab_mail_click()
    # time.sleep(1)
    # time.sleep(1)
    # page.tab_login_click()
    # time.sleep(1)