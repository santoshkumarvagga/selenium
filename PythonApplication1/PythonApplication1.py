import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Functionaltest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_occurence(self):

        # Navigating to web page by url or local path
        self.driver.get('C:\\Users\\Sahana Vagga\\source\\repos\\selenium\\PythonApplication1\\WebPage1.html')

        # Filling Forms
        ele = self.driver.find_element_by_id('fname')
        ele.clear()

        # Giving user input to input fields in form
        ele.send_keys('Santoshkumar')
        sec_ele = self.driver.find_element_by_id('lname')
        sec_ele.clear()
        sec_ele.send_keys('Vagga')

        # Dropdowns
        element = self.driver.find_element_by_xpath('/html/body/form/select')
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()

        # Form submit
        s = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        s.click()
        print('form passed')

    def tearDown(self):
        self.driver.quit()

unittest.main()