from .basepage import BasePage


class Catalog(BasePage):
    ELEMENT_MONITOR = "[src='https://demo.opencart.com/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']"
    SECOND_MONITOR = "[src='https://demo.opencart.com/image/cache/catalog/demo/samsung_syncmaster_941bw-228x228.jpg']"
    TITLE = "Monitors"
    LIST_VIEW = "[id='list-view']"
    PRODUCT_COMPARE = "[href='https://demo.opencart.com/index.php?route=product/compare']"

    def browser_url(browser):
        browser.get("https://demo.opencart.com/index.php?route=product/category&path=25_28")

    def element_monitor(browser):
        Catalog.browser_url(browser)
        BasePage.assert_element(Catalog.ELEMENT_MONITOR, browser)

    def element_second_monitor(browser):
        Catalog.browser_url(browser)
        BasePage.assert_element(Catalog.SECOND_MONITOR, browser)

    def title_catalog(browser):
        Catalog.browser_url(browser)
        BasePage.wait_title(Catalog.TITLE, browser)

    def element_list_view(browser):
        Catalog.browser_url(browser)
        BasePage.assert_element(Catalog.LIST_VIEW, browser)

    def element_product_compare(browser):
        Catalog.browser_url(browser)
        BasePage.assert_element(Catalog.PRODUCT_COMPARE, browser)
