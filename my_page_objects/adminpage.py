from .basepage import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT_LOGIN = "[name='username']"
    USERNAME_INPUT_PASSWORD = "[name='password']"
    LOGIN_LINK_FORGET_PASSWORD = "[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']"
    BUTTON_TYPE_SUBMIT = "[type='submit']"
    LOGIN_LINK_OPENCART = "[href='http://www.opencart.com']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/admin/")
