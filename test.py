import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import HtmlTestRunner

def setUpModule():
    print("Setting up module")

def tearDownModule():
    print("Tearing down module")

class PageTitleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Setting up class")
    
    @classmethod
    def tearDownClass(cls):
        print("Tearing down class")
    @classmethod
    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # run without opening a window
        self.driver = webdriver.Chrome(service=Service(), options=options)
        print("Setup complete")
    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Teardown complete")

    @unittest.skip('link' == 'link')
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        print("google title: " + self.driver.title)
        self.assertEqual(self.driver.title, "Google", "Title does not match")

    def test_facebook_title(self):
        self.driver.get("https://www.facebook.com")
        print("facebook title: " + self.driver.title)
        self.assertTrue("Facebook" in self.driver.title, "Title does not contain 'Facebook'")

    def test_Instagram_title(self):
        self.driver.get("https://www.instagram.com")
        print("Instagram title: " + self.driver.title)
        self.assertTrue("Instagram" in self.driver.title, "Title does not contain 'Instagram'")

    def test_x_title(self):
        self.driver.get("https://www.x.com")
        print("X title: " + self.driver.title)
        self.assertTrue("X" in self.driver.title, "Title does not contain 'X'")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./test_reports/'))