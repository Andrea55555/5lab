from my_page_objects.My_exceptions import assert_element
from my_page_objects.My_exceptions import wait_title


def test_element_first_name(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    assert_element("[name='firstname']", browser)


def test_title(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    wait_title("Register Account", browser)


def test_element_checkbox(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    assert_element("[name='agree']", browser)


def test_element_password(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    assert_element("[name='password']", browser)


def test_element_newsletter(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    assert_element("[name='newsletter']", browser)