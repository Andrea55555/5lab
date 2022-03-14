from my_page_objects.basepage import BasePage
from my_page_objects.adminpage import AdminPage
from my_page_objects.cardproduct import CardProduct
from my_page_objects.catalog import Catalog
from my_page_objects.main import Main
from my_page_objects.register_account import Register
from my_page_objects.registerpage import RegisterPage


def test_login_element(browser):
    AdminPage.login_element


def test_password_element(browser):
    AdminPage.password_element


def test_login_link_forget_password(browser):
    AdminPage.login_link_forget_password


def test_button_submit(browser):
    AdminPage.button_submit


def test_login_link_opencart(browser):
    AdminPage.login_link_opencart


def test_element_checkbox(browser):
    CardProduct.element_checkbox


def test_title_card_product(browser):
    CardProduct.title_card_product


def test_element_title_name(browser):
    CardProduct.element_title_name


def test_element_text_titles(browser):
    CardProduct.element_text_titles


def test_element_photo(browser):
    CardProduct.element_photo


def test_element_monitor(browser):
    Catalog.element_monitor


def test_element_second_monitor(browser):
    Catalog.element_second_monitor


def test_title_catalog(browser):
    Catalog.title_catalog


def test_element_list_view(browser):
    Catalog.element_list_view


def test_element_product_compare(browser):
    Catalog.element_product_compare


def test_element_search(browser):
    Main.element_search


def test_element_cameras(browser):
    Main.element_cameras


def test_image_phone(browser):
    Main.image_phone


def test_title(browser):
    Main.title


def test_elemesnt_search(browser):
    Main.elemesnt_search


def test_element_first_name(browser):
    Register.element_first_name


def test_title_register(browser):
    Register.title_register


def test_element_checkbox_register(browser):
    Register.element_checkbox_register


def test_element_password(browser):
    Register.element_password


def test_element_newsletter(browser):
    Register.element_newsletter


def test_user_registration(browser):
    register_page = RegisterPage(browser)
    register_page.open_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
