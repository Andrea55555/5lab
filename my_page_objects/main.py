from .basepage import BasePage


class Main(BasePage):
    SEARCH = "[name='search']"
    CAMERAS = "[href='https://demo.opencart.com/index.php?route=product/category&path=33']"
    PHONE = "[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-200x200.jpg']"
    TITLE = "Your Store"
    ELEMENT_SEARCH = "[src='https://demo.opencart.com/image/cache/catalog/demo/canon_eos_5d_1-200x200.jpg']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/")

    def element_search(browser):
        Main.browser_url(browser)
        BasePage.assert_element(Main.SEARCH, browser)

    def element_cameras(browser):
        Main.browser_url(browser)
        BasePage.assert_element(Main.CAMERAS, browser)

    def image_phone(browser):
        Main.browser_url(browser)
        BasePage.assert_element(Main.PHONE, browser)

    def title(browser):
        Main.browser_url(browser)
        BasePage.wait_title(Main.TITLE, browser)

    def elemesnt_search(browser):
        Main.browser_url(browser)
        BasePage.assert_element(Main.ELEMENT_SEARCH, browser)
