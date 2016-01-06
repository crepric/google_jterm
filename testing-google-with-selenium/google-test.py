import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Smith College")
        elem.send_keys(Keys.RETURN)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ires"))
                )
            self.assertIn("www.smith.edu", element.text)
        except:
            self.assertTrue(False)

    def test_search_in_google_implicit(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Smith College")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(10) # seconds
        results = driver.find_element_by_id("ires")
        self.assertIn("www.smith.edu", results.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
