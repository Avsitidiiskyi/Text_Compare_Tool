import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

class GoogleSearch(unittest.TestCase):
    def setUp(self):

     self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_1(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        input_field = driver.find_element_by_id('fakebox-input')
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)

        titles = driver.find_elements_by_class_name('r')
        for title in titles:
            assert "python" in title.text.lower()



    def test_2(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name('fakebox-input')
        input_field.send_keys('python')
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.ENTER)


titles = driver.find_elements_by_class_name('r')
for title in titles:
    assert "python" in title.text.lower()


    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get('http://google.com')
# assert "Google" in driver.page_source
# #
# if 'Google' in driver.page_source:
#
#     print('got it')
# else:
#     print('fail')
#
# driver.quit()
#




