from selenium import webdriver
import unittest


class CommonUnitTests(unittest.TestCase):
# Your code here


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CommonUnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
