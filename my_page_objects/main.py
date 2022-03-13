from .basepage import BasePage


class Main(BasePage):
    SEARCH = "[name='search']"
    CAMERAS = "[href='https://demo.opencart.com/index.php?route=product/category&path=33']"
    PHONE = "[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-200x200.jpg']"
    TITLE = "Your Store"
    ELEMENT_SEARCH = "[src='https://demo.opencart.com/image/cache/catalog/demo/canon_eos_5d_1-200x200.jpg']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/")

