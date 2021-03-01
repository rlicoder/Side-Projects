from selenium import webdriver
from time import sleep
import sys
import selenium.common.exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gettime import *

bot = webdriver.Firefox()
bot.set_window_size(1600, 1000)

bot.get('https://v2.waitwhile.com/welcome/microcentertust')

while True:
    try:
        WebDriverWait(bot, 10).until(EC.visibility_of(bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')))
        html = bot.page_source
        if html.find('Waitlist is currently closed') != -1:
            bot.refresh()
        else:
            break
    except Exception as e:
        pass

bot.save_screenshot('waitlist opened ' + gettime() + '.png')

join = bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')

join.click()

bot.save_screenshot('joined queue ' + gettime() + '.png')

f = open('info.txt', 'r')
num_people = int(f.readline())
while True:
    try:
        add = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-partysize/div/section/div[2]/div[1]/div[2]')
        for i in range (1, num_people):
            add.click()
        break
    except (ex.ElementClickInterceptedException, ex.NoSuchElementException) as e:
        continue

bot.save_screenshot('party size ' + gettime() + '.png')

while True:
    try:
        next_button = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-partysize/div/section/div[2]/div[2]/button')
        next_button.click()
        break
    except (ex.ElementClickInterceptedException, ex.NoSuchElementException) as e:
        continue;
    
bot.save_screenshot('before filling form ' + gettime() + '.png')

firstname = str(f.readline())
lastname = str(f.readline())
phonenum = str(f.readline())

while True:
    try:
        first = bot.find_element_by_xpath('//*[@id="name02"]')
        first.send_keys(firstname)
        last = bot.find_element_by_xpath('//*[@id="name03"]')
        last.send_keys(lastname)
        phone = bot.find_element_by_xpath('//*[@id="phone01"]')
        phone.send_keys(phonenum)
        break
    except (ex.ElementClickInterceptedException, ex.NoSuchElementException) as e:
        continue
f.close()

bot.save_screenshot('after filling form ' + gettime() + '.png')

drop = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/div')
drop.click()

bot.save_screenshot('clicked dropdown ' + gettime() + '.png')

webdriver.ActionChains(bot).move_to_element(drop).perform()
webdriver.ActionChains(bot).move_by_offset(0, 50).perform()
webdriver.ActionChains(bot).click().perform()

bot.save_screenshot('clicked option ' + gettime() + '.png')

confirm = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/button')
confirm.click()

bot.save_screenshot('confirmed ' + gettime() + '.png')

