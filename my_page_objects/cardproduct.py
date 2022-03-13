from .basepage import BasePage


class CardProduct(BasePage):
    ELEMENT_CHECKBOX = "[name='option[223][]']"
    TITLE = "Apple Cinema 30"
    TITLE_NAME = "[name='option[208]']"
    TITLE_TEXT = "[face='Helvetica']"
    ELEMENT_PHOTO = "[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/index.php?route=product/product&path=25_28&product_id=42")

