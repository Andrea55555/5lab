from my_page_objects.My_exceptions import assert_element
from my_page_objects.My_exceptions import wait_title

def test_element_search(browser):
    browser.get("https://demo.opencart.com/")
    assert_element("[name='search']", browser)


def test_element_cameras(browser):
    browser.get("https://demo.opencart.com/")
    assert_element("[href='https://demo.opencart.com/index.php?route=product/category&path=33']", browser)


def test_image_phone(browser):
    browser.get("https://demo.opencart.com/")
    assert_element("[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-200x200.jpg']", browser)


def test_title(browser):
    browser.get("https://demo.opencart.com/")
    wait_title("Your Store", browser)


def test_elemesnt_search(browser):
    browser.get("https://demo.opencart.com/")
    assert_element("[src='https://demo.opencart.com/image/cache/catalog/demo/canon_eos_5d_1-200x200.jpg']", browser)