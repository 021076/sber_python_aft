import time
from selenium import webdriver
import pytest
import requests
#
def test_sber():
    browser = webdriver.Edge()
    browser.delete_all_cookies()
    # ожидаемое время для поиска элемента
    browser.implicitly_wait(20)
    browser.get("http://sberbank.ru")
    browser.maximize_window()
    time.sleep(5)