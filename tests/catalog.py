from my_page_objects.My_exceptions import assert_element
from my_page_objects.My_exceptions import wait_title

def test_element_monitor(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")
    assert_element("[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']", browser)


def test_element_second_monitor(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")
    assert_element("[src='https://demo.opencart.com/image/cache/catalog/demo/samsung_syncmaster_941bw-228x228.jpg']", browser)


def test_title(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")
    wait_title("Monitors", browser)


def test_element_list_view(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")
    assert_element("[id='list-view']", browser)


def test_element_product_compare(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")
    assert_element("[href='https://demo.opencart.com/index.php?route=product/compare']", browser)