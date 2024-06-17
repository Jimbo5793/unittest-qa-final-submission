import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from app import app


class TestCoinChangeUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate thread
        cls.app_thread = threading.Thread(target=app.run, kwargs={'debug': False, 'use_reloader': False})
        cls.app_thread.daemon = True
        cls.app_thread.start()
        time.sleep(1) 

        # Initialize the Selenium WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10) 

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://127.0.0.1:5000/') 

    def test_basic_functionality(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: [1, 2, 5], 11 -> 3
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('1,2,5')
        amount_input.send_keys('11')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        result_text = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn('Result: 3', result_text)

    def test_invalid_coins_input(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: invalid coins input -> error
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('a,b,c')
        amount_input.send_keys('11')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        error_text = driver.find_element(By.XPATH, '//h2[@style="color: red;"]').text
        self.assertIn('Error:', error_text)

    def test_edge_case_large_amount(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: [1], 10000 -> 10000
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('1')
        amount_input.send_keys('10000')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        result_text = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn('Result: 10000', result_text)

    def test_edge_case_large_coin_value(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: invalid coin value -> error
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('2147483648')
        amount_input.send_keys('10')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        error_text = driver.find_element(By.XPATH, '//h2[@style="color: red;"]').text
        self.assertIn('Error:', error_text)

    def test_edge_case_large_number_of_coins(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: too many coins -> error
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('1,2,3,4,5,6,7,8,9,10,11,12,13')
        amount_input.send_keys('10')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        error_text = driver.find_element(By.XPATH, '//h2[@style="color: red;"]').text
        self.assertIn('Error:', error_text)

    def test_edge_case_negative_amount(self):
        driver = self.driver

        coins_input = driver.find_element(By.ID, 'coins')
        amount_input = driver.find_element(By.ID, 'amount')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        # Test case: negative amount -> error
        coins_input.clear()
        amount_input.clear()
        coins_input.send_keys('1,2,3')
        amount_input.send_keys('-1')
        submit_button.click()
        time.sleep(1)  # Allow time for processing
        error_text = driver.find_element(By.XPATH, '//h2[@style="color: red;"]').text
        self.assertIn('Error:', error_text)


if __name__ == '__main__':
    unittest.main()
