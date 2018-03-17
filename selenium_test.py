#! /usr/bin/env python
import unittest
from selenium import webdriver

#browser = webdriver.Firefox()
class TestSamsLinkedin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def testTitle(self):
        self.browser.get('https://www.linkedin.com/in/samuel-rosen-108a8577')
        self.assertIn('Samuel Rosen',self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

