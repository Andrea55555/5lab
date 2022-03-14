from .basepage import BasePage


class CardProduct(BasePage):
    ELEMENT_CHECKBOX = "[name='option[223][]']"
    TITLE = "Apple Cinema 30"
    TITLE_NAME = "[name='option[208]']"
    TITLE_TEXT = "[face='Helvetica']"
    ELEMENT_PHOTO = "[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")

    def element_checkbox(browser):
        CardProduct.browser_url(browser)
        BasePage.assert_element(CardProduct.ELEMENT_CHECKBOX, browser)

    def title_card_product(browser):
        CardProduct.browser_url(browser)
        BasePage.wait_title(CardProduct.TITLE, browser)

    def element_title_name(browser):
        CardProduct.browser_url(browser)
        BasePage.assert_element(CardProduct.TITLE_NAME, browser)

    def element_text_titles(browser):
        CardProduct.browser_url(browser)
        BasePage.assert_element(CardProduct.TITLE_TEXT, browser)

    def element_photo(browser):
        CardProduct.browser_url(browser)
        BasePage.assert_element(CardProduct.ELEMENT_PHOTO, browser)
