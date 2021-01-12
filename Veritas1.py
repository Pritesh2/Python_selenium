from selenium import webdriver

import unittest
import HtmlTestRunner

# unit test features : to do

#  to launch the browser
# verify home page title
# verify login
# to close the browser

class Veritas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox(executable_path='/home/pritesh/Desktop/Veritas_Python/geckodriver-v0.27.0-linux64/geckodriver')
        cls.driver.maximize_window()

    def test_verify_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"Webpage title not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()

        # once we clicked the submit button we again verify whether we land on some page or not
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title not matching")
        #self.assertEqual()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # close all the windows
        print("Test is now completed")

if __name__=='__main__':
    unittest.main()

