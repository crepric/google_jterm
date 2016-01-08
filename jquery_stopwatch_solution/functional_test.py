import os
import time
from selenium import webdriver
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click_and_wait(self):
        driver = self.driver
        current_folder = os.path.dirname(os.path.realpath(__file__))
        driver.get("file:///" + current_folder + "/index.html")
        # Find the start and stop button and check that stop does not appear.
        start_button = driver.find_element_by_id("start")
        stop_button = driver.find_element_by_id("stop")
        self.assertFalse(stop_button.is_displayed())
        self.assertTrue(start_button.is_displayed())
        # Click on start
        start_button.click()
        # Verify that the button has disappeared and stop is now visible.
        self.assertFalse(start_button.is_displayed())
        self.assertTrue(stop_button.is_displayed())
        time.sleep(10);
        stop_button.click()
        # check if value has been updated by at least 10 (to be safe we will
        # also accept 11, since the test might have taken some time)
        self.assertFalse(stop_button.is_displayed())
        self.assertTrue(start_button.is_displayed())
        counter_value = int(driver.find_element_by_id("counter").text)
        self.assertGreaterEqual(counter_value, 10)
        self.assertLessEqual(counter_value, 11)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
