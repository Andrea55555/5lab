from my_page_objects.My_exceptions import assert_element
from my_page_objects.My_exceptions import wait_title


def test_element_checkbox(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")
    assert_element("[name='option[223][]']", browser)


def test_title(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")
    wait_title("Apple Cinema 30", browser)


def test_element_title_name(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")
    assert_element("[name='option[208]']", browser)


def test_element_text_titles(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")
    assert_element(("[face='Helvetica']"), browser)


def test_element_photo(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")
    assert_element("[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']", browser)
