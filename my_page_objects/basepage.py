from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _verify_element_visibility(self, locator, time=3):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find element by locator: {locator}")

    def _find_element_and_click(self, locator):
        element = self._verify_element_visibility(locator)
        element.click()

    def _fill_input_field(self, field, text):
        field = self._verify_element_visibility(field)
        field.click()
        field.clear()
        field.send_keys(text)
