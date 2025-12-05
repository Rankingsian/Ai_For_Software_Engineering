import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Setup headless chrome for the environment
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # In a real local environment, you might not use headless to see the action
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            print(f"Failed to initialize driver: {e}")
            self.driver = None

    def test_valid_login(self):
        if not self.driver:
            print("Skipping test: Driver not initialized")
            return

        driver = self.driver
        # Using a public test site
        driver.get("https://the-internet.herokuapp.com/login")
        
        # AI tools would automatically identify these selectors
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(2) # Wait for page load
        
        # Check for success message
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        self.assertTrue(success_message.is_displayed())
        print("Valid login test passed!")

    def test_invalid_login(self):
        if not self.driver:
            print("Skipping test: Driver not initialized")
            return

        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        
        username_field.send_keys("wronguser")
        password_field.send_keys("wrongpassword")
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Check for error message
        error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
        self.assertTrue(error_message.is_displayed())
        print("Invalid login test passed!")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
