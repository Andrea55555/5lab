import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def wait_title(title, driver, timeout=3):
        title.logger.info(f"wait element {driver.title}")
        try:
            WebDriverWait(driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            # Выбрасываю своё исключение и добавляю сообщение
            raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))

    def assert_element(selector, driver, timeout=1, by=By.CSS_SELECTOR):
        selector.logger.info(f"search element{format(selector)}")
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, selector)))
        except TimeoutException:
            driver.save_screenshot("{}.png".format(driver.session_id))
            raise AssertionError("Не дождался видимости элемента: {}".format(selector))

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    def _verify_element_visibility(self, locator, time=3):
        self.logger.info(f"Check if element {locator} is present")
        with allure.step(f"Элемент {locator} присутствует на странице и виден юзеру"):
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                           message=f"Can't find element by locator: {locator}")

    @allure.step("Клик по элементу на странице")
    def _find_element_and_click(self, locator):
        self.logger.info(f"Check if element {locator} is present and click")
        element = self._verify_element_visibility(locator)
        element.click()

    def _fill_input_field(self, field, text):
        self.logger.info(f"Input {text} in input {field}")
        field = self._verify_element_visibility(field)
        field.click()
        field.clear()
        field.send_keys(text)
