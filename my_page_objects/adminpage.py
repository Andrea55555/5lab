from .basepage import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT_LOGIN = "[name='username']"
    USERNAME_INPUT_PASSWORD = "[name='password']"
    LOGIN_LINK_FORGET_PASSWORD = "[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']"
    BUTTON_TYPE_SUBMIT = "[type='submit']"
    LOGIN_LINK_OPENCART = "[href='http://www.opencart.com']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/admin/")

    def login_element(browser):
        AdminPage.browser_url(browser)
        BasePage.assert_element(AdminPage.USERNAME_INPUT_LOGIN, browser)

    def password_element(browser):
        AdminPage.browser_url(browser)
        BasePage.assert_element(AdminPage.USERNAME_INPUT_PASSWORD, browser)

    def login_link_forget_password(browser):
        AdminPage.browser_url(browser)
        BasePage.assert_element(AdminPage.LOGIN_LINK_FORGET_PASSWORD, browser)

    def button_submit(browser):
        AdminPage.browser_url(browser)
        BasePage.assert_element(AdminPage.BUTTON_TYPE_SUBMIT, browser)

    def login_link_opencart(browser):
        AdminPage.browser_url(browser)
        BasePage.assert_element(AdminPage.LOGIN_LINK_OPENCART, browser)
