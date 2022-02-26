from my_page_objects.My_exceptions import assert_element


def test_login_element(browser):
    browser.get("https://demo.opencart.com/admin/")
    assert_element("[name='username']", browser)


def test_password_element(browser):
    browser.get("https://demo.opencart.com/admin/")
    assert_element("[name='password']", browser)


def test_login_link_forget_password(browser):
    browser.get("https://demo.opencart.com/admin/")
    assert_element("[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']", browser)


def test_button_submit(browser):
    browser.get("https://demo.opencart.com/admin/")
    assert_element("[type='submit']", browser)


def test_login_link_opencart(browser):
    browser.get("https://demo.opencart.com/admin/")
    assert_element("[href='http://www.opencart.com']", browser)