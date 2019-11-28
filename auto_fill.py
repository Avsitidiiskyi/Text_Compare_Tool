import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import choice
from string import ascii_letters

# def phone():
#     var_code = [+3896, +38050, +38097, +38098, +38073, +38099]
#     code = random.choice(var_code)
#     num = (random.randrange(10, 9000000, 5))
#     result ='+'+str(code) + str(num)
#     return result
mail_name = ['Olivia','Noah','Ethan','Mason','Logan','Lucas','Jacob','Jackson','Aiden',
'Jack',
'Luke',
'Elijah',
'Benjamin',
'James',
'William',
'Michael',
'Alexander',
'Oliver',
'Daniel',
'Henry',
'Owen',
'Gabriel',
'Matthew',
'Carter',
'Ryan',
'Wyatt',
'Andrew',
'Caleb',
'Jayden',
'Connor',
'Liam',
'Emma',
'Sophia',
'Ava',
'Isabella',
'Mia',
'Charlotte',
'Emily',
'Harper',
'Abigail',
'Madison',
'Avery',
'Ella',
'Madison',
'Lily',
'Chloe',
'Sofia',
'Evelyn',
'Hannah',
'Addison',
'Grace',
'Zoey',
'Aubrey',
'Aria',
'Zoe',
'Ellie',
'Audrey',
'Natalie',
'Elizabeth',
'Scarlett',
]
domains = ['@gmail.com', '@mail.ru','@I.ua','@yahoo.com','@meta.ua', '@icloud.com', '@ukr.net','@yandex.ru']
def e_mail():
   first_email_part = (''.join(choice(ascii_letters) for i in range(4)))
   second_email_part = random.choice(mail_name)
   final_part = random.choice(domains)
   result = str(first_email_part) + str(second_email_part)+ str(final_part)
   return result
#_______________________EMAIL FUNCTION______________________________________



name_list = ['Иван', 'Гена', 'Кирилл', 'Валентина', 'Дима', 'Ашот', 'Андрей',
'Павел',
'Паисий',
'Пантелеймон',
'Парфений',
'Пафнутий',
'Пахомий',
'Пётр',
'Платон',
'Порфирий',
'Потап',
'Пров',
'Прокопий',
'Протасий',
'Прохор',

'Вазген', 'Эдурд', 'Виталик', 'Марина', 'Элона', 'Илья', 'Володя', 'Артем', 'Василий', 'Гриша',
'Леонид', 'Назар', 'Юрка', 'Алёна', 'Алина', 'Димас', 'Максим'  ]
def char_name():
    name = random.choice(name_list)
    return name







def phone():
    var_code = [96, 50, 97, 98, 73, 99]
    code = random.choice(var_code)
    num = (random.randrange(9000000))
    result = str(code) + str(num)
    return result
#_________________Phone_function_________________




# print(char_name())
# print(str(phone()))
#______________________________

site= 'xxx'
account = '/html/body/div[1]/div[2]/nonutch/div/div[2]/div[2]/div/div[2]/div/a[1]'

class some_site(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_TT_signUP(self):
        self.driver.get(site)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mdl-subcribe-uk"]/button').click()


        self.driver.find_element_by_xpath(account).click()
        name=self.driver.find_element_by_id('render_form_name')
        name.send_keys(char_name())
        sleep(3)

        email = self.driver.find_element_by_id('render_form_email')
        email.send_keys(e_mail())
        sleep(5)

        fone = self.driver.find_element_by_id('render_form_phone')
        fone.send_keys(phone())

        sleep(7)
        #
        # self.driver.find_element_by_class_name('select2-selection__rendered').click() #//*[@id="select2-render_form_office_id-container"]
        # sleep(2)
        # office = self.driver.find_element_by_class_name('select2-selection__rendered')
        # office.send_keys(Keys.DOWN)
        # sleep(3)
        # office.send_keys(Keys.ENTER)
        # sleep(2)
        self.driver.find_element_by_id('render_form_submit').click()
        sleep(50)
#
    # def tearDown(self):
    #         self.driver.quit()

if __name__ == '__main__':
        unittest.main()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
