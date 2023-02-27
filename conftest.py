import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def selenium():
    driver = webdriver.Chrome("C:/Users/Руслан/PycharmProjects/FinalWork/chromedriver.exe")
    driver.get('https://b2c.passport.rt.ru/')

    yield driver

    driver.quit()