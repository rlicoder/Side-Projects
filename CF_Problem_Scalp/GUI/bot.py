from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime

def createVJudge():
    bot = webdriver.Firefox()

    bot.set_page_load_timeout(10)
    bot.get('https://vjudge.net/')

    while (True):
        try:
            bot.find_element_by_xpath('/html/body/nav/div/ul/li[8]/a').click()
            break
        except Exception as e:
            print(e)

    while(True):
        try:
            bot.find_element_by_id('login-username').send_keys('iforgotmyaccount')
            bot.find_element_by_id('login-password').send_keys('iforgotmyaccount')
            bot.find_element_by_id('btn-login').click()
            break
        except Exception as e:
            print(e)
            time.sleep(1)

    while (True):
        try:
            bot.find_element_by_xpath('/html/body/nav/div/ul/li[3]/a').click()
            break
        except Exception as e:
            time.sleep(1)

    while (True):
        try:
            bot.find_element_by_id('btn-create').click()
            time.sleep(.75)
            bot.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
            time.sleep(.75)
            bot.find_element_by_id('btn-create').click()
            time.sleep(.75)
            break
        except Exception as e:
            print(e)
            time.sleep(1)

    while (True):
        try: 
            dropdown = Select(bot.find_element_by_id('contest-openness'))
            dropdown.select_by_value('2')
            bot.find_element_by_id('contest-title').send_keys('title')
            bot.find_element_by_id('contest-password').send_keys('password')
            contest_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
            bot.find_element_by_id('contest-begin-time').clear()
            bot.find_element_by_id('contest-begin-time').send_keys(str(contest_time)[:-7])
            bot.find_element_by_id('contest-length').clear()
            bot.find_element_by_id('contest-length').send_keys('1:2:3')
            bot.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/nav/ul/li[2]/a').click()
            break
        except Exception as e:
            print (e)
            time.sleep(1)

    while (True):
        try:
            OJ = Select(bot.find_element_by_id([contains('oj-')]))
            OJ.select_by_value('CodeForces')
            add = bot.find_element_by_id('addBtn')
            base_table = '/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/input[1]'
            for i in range (0, 10):
                add.click()
                strlist = list(base_table)
                strlist[-17] = chr(i+1)
                base_table = ''.join(strlist)
                bot.find_element_by_xpath(base_table).send_keys('x')
        except Exception as e:
            print(e)


