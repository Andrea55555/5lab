import allure

from my_page_objects.adminpage import AdminPage
from my_page_objects.cardproduct import CardProduct
from my_page_objects.catalog import Catalog
from my_page_objects.main import Main
from my_page_objects.register_account import Register
from my_page_objects.registerpage import RegisterPage


@allure.title("test_login_element")
def test_login_element(browser):
    AdminPage.login_element


@allure.title("test_password_element")
def test_password_element(browser):
    AdminPage.password_element


@allure.title("test_login_link_forget_password")
def test_login_link_forget_password(browser):
    AdminPage.login_link_forget_password


@allure.title("test_button_submit")
def test_button_submit(browser):
    AdminPage.button_submit


@allure.title("test_login_link_opencart")
def test_login_link_opencart(browser):
    AdminPage.login_link_opencart


@allure.title("test_element_checkbox")
def test_element_checkbox(browser):
    CardProduct.element_checkbox


@allure.title("test_title_card_product")
def test_title_card_product(browser):
    CardProduct.title_card_product


@allure.title("test_element_title_name")
def test_element_title_name(browser):
    CardProduct.element_title_name


@allure.title("test_element_text_titles")
def test_element_text_titles(browser):
    CardProduct.element_text_titles


@allure.title("test_element_photo")
def test_element_photo(browser):
    CardProduct.element_photo


@allure.title("test_element_monitor")
def test_element_monitor(browser):
    Catalog.element_monitor


@allure.title("test_element_second_monitor")
def test_element_second_monitor(browser):
    Catalog.element_second_monitor


@allure.title("test_title_catalog")
def test_title_catalog(browser):
    Catalog.title_catalog


@allure.title("test_element_list_view")
def test_element_list_view(browser):
    Catalog.element_list_view


@allure.title("test_element_product_compare")
def test_element_product_compare(browser):
    Catalog.element_product_compare


@allure.title("test_element_search")
def test_element_search(browser):
    Main.element_search


@allure.title("test_element_cameras")
def test_element_cameras(browser):
    Main.element_cameras


@allure.title("test_image_phone")
def test_image_phone(browser):
    Main.image_phone


@allure.title("test_title")
def test_title(browser):
    Main.title


@allure.title("test_elemesnt_search")
def test_elemesnt_search(browser):
    Main.elemesnt_search


@allure.title("test_element_first_name")
def test_element_first_name(browser):
    Register.element_first_name


@allure.title("test_title_register")
def test_title_register(browser):
    Register.title_register


@allure.title("test_element_checkbox_register")
def test_element_checkbox_register(browser):
    Register.element_checkbox_register


@allure.title("test_element_password")
def test_element_password(browser):
    Register.element_password


@allure.title("test_element_newsletter")
def test_element_newsletter(browser):
    Register.element_newsletter


@allure.story("Registration")
@allure.title("test_user_registration")
def test_user_registration(browser):
    register_page = RegisterPage(browser)
    register_page.open_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
