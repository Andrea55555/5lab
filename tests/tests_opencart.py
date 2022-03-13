from my_page_objects.basepage import BasePage
from my_page_objects.adminpage import AdminPage
from my_page_objects.cardproduct import CardProduct
from my_page_objects.catalog import Catalog
from my_page_objects.main import Main
from my_page_objects.register_account import Register
from my_page_objects.registerpage import RegisterPage


def test_login_element(browser):
    AdminPage.browser_url(browser)
    BasePage.assert_element(AdminPage.USERNAME_INPUT_LOGIN, browser)


def test_password_element(browser):
    AdminPage.browser_url(browser)
    BasePage.assert_element(AdminPage.USERNAME_INPUT_PASSWORD, browser)


def test_login_link_forget_password(browser):
    AdminPage.browser_url(browser)
    BasePage.assert_element(AdminPage.LOGIN_LINK_FORGET_PASSWORD, browser)


def test_button_submit(browser):
    AdminPage.browser_url(browser)
    BasePage.assert_element(AdminPage.BUTTON_TYPE_SUBMIT, browser)


def test_login_link_opencart(browser):
    AdminPage.browser_url(browser)
    BasePage.assert_element(AdminPage.LOGIN_LINK_OPENCART, browser)


def test_element_checkbox(browser):
    CardProduct.browser_url(browser)
    BasePage.assert_element(CardProduct.ELEMENT_CHECKBOX, browser)


def test_title_card_product(browser):
    CardProduct.browser_url(browser)
    BasePage.wait_title(CardProduct.TITLE, browser)


def test_element_title_name(browser):
    CardProduct.browser_url(browser)
    BasePage.assert_element(CardProduct.TITLE_NAME, browser)


def test_element_text_titles(browser):
    CardProduct.browser_url(browser)
    BasePage.assert_element(CardProduct.TITLE_TEXT, browser)


def test_element_photo(browser):
    CardProduct.browser_url(browser)
    BasePage.assert_element(CardProduct.ELEMENT_PHOTO, browser)


def test_element_monitor(browser):
    Catalog.browser_url(browser)
    BasePage.assert_element(Catalog.ELEMENT_MONITOR, browser)


def test_element_second_monitor(browser):
    Catalog.browser_url(browser)
    BasePage.assert_element(Catalog.SECOND_MONITOR, browser)


def test_title_catalog(browser):
    Catalog.browser_url(browser)
    BasePage.wait_title(Catalog.TITLE, browser)


def test_element_list_view(browser):
    Catalog.browser_url(browser)
    BasePage.assert_element(Catalog.LIST_VIEW, browser)


def test_element_product_compare(browser):
    Catalog.browser_url(browser)
    BasePage.assert_element(Catalog.PRODUCT_COMPARE, browser)


def test_element_search(browser):
    Main.browser_url(browser)
    BasePage.assert_element(Main.SEARCH, browser)


def test_element_cameras(browser):
    Main.browser_url(browser)
    BasePage.assert_element(Main.CAMERAS, browser)


def test_image_phone(browser):
    Main.browser_url(browser)
    BasePage.assert_element(Main.PHONE, browser)


def test_title(browser):
    Main.browser_url(browser)
    BasePage.wait_title(Main.TITLE, browser)


def test_elemesnt_search(browser):
    Main.browser_url(browser)
    BasePage.assert_element(Main.ELEMENT_SEARCH, browser)


def test_element_first_name(browser):
    Register.browser_url(browser)
    BasePage.assert_element(Register.FIRST_NAME, browser)


def test_title_register(browser):
    Register.browser_url(browser)
    BasePage.wait_title(Register.TITLE, browser)


def test_element_checkbox_register(browser):
    Register.browser_url(browser)
    BasePage.assert_element(Register.CHECKBOX, browser)


def test_element_password(browser):
    Register.browser_url(browser)
    BasePage.assert_element(Register.PASSWORD, browser)


def test_element_newsletter(browser):
    Register.browser_url(browser)
    BasePage.assert_element(Register.NEWSLETTER, browser)


def test_user_registration(browser):
    register_page = RegisterPage(browser)
    register_page.open_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
