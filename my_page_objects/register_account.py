from .basepage import BasePage


class Register(BasePage):
    FIRST_NAME = "[name='firstname']"
    TITLE = "Register Account"
    CHECKBOX = "[name='agree']"
    PASSWORD = "[name='password']"
    NEWSLETTER = "[name='newsletter']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/index.php?route=account/register")

    def element_first_name(browser):
        Register.browser_url(browser)
        BasePage.assert_element(Register.FIRST_NAME, browser)

    def title_register(browser):
        Register.browser_url(browser)
        BasePage.wait_title(Register.TITLE, browser)

    def element_checkbox_register(browser):
        Register.browser_url(browser)
        BasePage.assert_element(Register.CHECKBOX, browser)

    def element_password(browser):
        Register.browser_url(browser)
        BasePage.assert_element(Register.PASSWORD, browser)

    def element_newsletter(browser):
        Register.browser_url(browser)
        BasePage.assert_element(Register.NEWSLETTER, browser)
