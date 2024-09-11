import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from GoogleFinancePage import GoogleFinancePage

class GoogleFinanceTest(unittest.TestCase):
    def setUp(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized

        # Initialize the WebDriver with Chrome options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.google.com/finance/")
        self.google_finance_page = GoogleFinancePage(self.driver)

    def test_page_loaded(self):
        self.assertTrue(self.google_finance_page.is_loaded(), "Google Finance page did not load correctly")

    def test_stock_symbols(self):
        # Given test data
        given_test_data = ["NFLX", "MSFT", "TSLA"]  # Can add more as needed

        # Retrieve stock symbols from the webpage
        stock_symbols = self.google_finance_page.get_stock_symbols()

        # Find and print symbols in the webpage but not in given test data
        not_in_test_data = [symbol for symbol in stock_symbols if symbol not in given_test_data]
        print("Symbols in webpage but not in given test data:", not_in_test_data)

        # Find and print symbols in given test data but not in the webpage
        not_in_web_data = [symbol for symbol in given_test_data if symbol not in stock_symbols]
        print("Symbols in given test data but not in webpage:", not_in_web_data)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
