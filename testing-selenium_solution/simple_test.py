from selenium import webdriver
import unittest

# This test actually runs twice, as you can see at the bottom of this file,
# With the browser open at different sizes, so we can check that some invariants
# such that the links are 3 are not influenced by the size of the screen.
class CommonUnitTests(unittest.TestCase):
    browser_width = 1024
    browser_height = 800

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.set_window_size(cls.browser_width, cls.browser_height)
        cls.browser.get('file:///Users/crepric/jterm/code/testing-selenium/simple.html')

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTitle(self):
        self.assertIn('Test!', self.browser.title)

    def testLinkCount(self):
        links = self.browser.find_elements_by_css_selector('nav a')
        self.assertEqual(3, len(links))

    def testLinkOrder(self):
        expected_order = ["#1", "#2", "#3"]
        links = self.browser.find_elements_by_css_selector('nav a')
        for idx in range(len(expected_order)):
            self.assertIn(expected_order[idx], links[idx].get_attribute("href"))


if __name__ == "__main__":
    sizes = [
                (1024, 768),
                (420, 700),
            ]
    for size in sizes:
        CommonUnitTests.browser_width = size[0]
        CommonUnitTests.browser_height = size[1]
        suite = unittest.TestLoader().loadTestsFromTestCase(CommonUnitTests)
        unittest.TextTestRunner().run(suite)
