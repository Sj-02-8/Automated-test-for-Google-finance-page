from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.title = "Google Finance"
        self.interested_in_section_locator = (By.XPATH, "//div[contains(text(), 'You may be interested in')]/following-sibling::div")

    def is_loaded(self):
        return self.title in self.driver.title

    def get_stock_symbols(self):
        interested_in_section = self.wait.until(EC.presence_of_element_located(self.interested_in_section_locator))
        stock_symbols = interested_in_section.find_elements(By.XPATH, ".//a/div/div[2]/div[1]")
        return [symbol.text for symbol in stock_symbols]
