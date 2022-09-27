import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
         ]

@pytest.mark.parametrize('site', links)
def test_check_product_page_contains_cart_button(browser, site):
    link = site
    browser.maximize_window()
    browser.get(link)
    button_basket = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    time.sleep(30)

    assert button_basket.text == "Añadir al carrito" or button_basket.text == "Add to basket", f"Esta no es una localización en español o inglés del sitio!\nThis is not a Spanish or English localization of the site!"


