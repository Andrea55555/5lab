from .basepage import BasePage


class Register(BasePage):
    FIRST_NAME = "[name='firstname']"
    TITLE = "Register Account"
    CHECKBOX = "[name='agree']"
    PASSWORD = "[name='password']"
    NEWSLETTER = "[name='newsletter']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/index.php?route=account/register")

