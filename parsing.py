from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Name_gen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()#ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_parse(self):
        self.driver.get("http://megagenerator.ru/namefio/")
        sleep(10)
        sleep(2)

        value_gen = self.driver.find_element_by_name('vvod')
        value_gen.send_keys('1000')
        sleep(2)

        country = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[3]/div[1]/div/input')
        country.send_keys(Keys.DOWN)
        sleep(2)
        country.send_keys(Keys.ENTER)
        sleep(1)

        self.driver.find_element_by_id('generate').click()
        sleep(2)

        title = self.driver.find_element_by_id('result')  # parses test from element
        print(title.text)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__': # won't start without that code part
        unittest.main()

























# class Name_gen(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()#ChromeDriverManager().install())
#         self.driver.maximize_window()
#
#     def test_parse(self):
#         self.driver.get("https://generator-online.com/names//") #(http://megagenerator.ru/namefio/)
#         sleep(2)
#         self.driver.find_element_by_xpath('/html/body/div[1]/div/main/div/section/div[1]/div[1]/div[2]/span[1]/label/span').click()
#         sleep(2)
#         self.driver.find_element_by_xpath('/html/body/div[1]/div/main/div/section/div[1]/div[1]/div[2]/span[3]/label/span').click()
#         sleep(2)
#         self.driver.find_element_by_id('genbutton').click()
#         sleep(2)
#
#         title = self.driver.find_element_by_id('namesresult')  # parses test from element
#         print(title.text)
#
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__': # won't start without that code part
#         unittest.main()
#
#














