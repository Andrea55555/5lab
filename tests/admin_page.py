from page_objects.LoginAdminPage import LoginAdminPage


def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)


def test_correct_all(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()


def test_incorrect_login(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user3")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()


def test_incorrect_password(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami3")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
