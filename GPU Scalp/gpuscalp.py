from selenium import webdriver
from time import sleep
import sys
import selenium.common.exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gettime import *
from selenium.webdriver.common.keys import Keys

bot = webdriver.Firefox()
bot.set_window_size(1600, 1000)

bot.get('https://v2.waitwhile.com/welcome/microcentertust')

while True:
    try:
        WebDriverWait(bot, 30).until(EC.visibility_of(bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')))
        html = bot.page_source
        if html.find('Waitlist is currently closed') != -1:
            bot.execute_script('window.location.reload(true)')
            sleep(1)
        else:
            break
    except Exception as e:
        pass


while True:
    try:
        bot.save_screenshot('waitlist opened ' + gettime() + '.png')
        join = bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
        join.click()
        break;
    except Exception:
        continue


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

while True:
    try:
        drop = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/div')
        drop.click()
        break
    except Exception:
        continue

bot.save_screenshot('clicked dropdown ' + gettime() + '.png')

while True:
    try:
        webdriver.ActionChains(bot).move_to_element(drop).perform()
        webdriver.ActionChains(bot).move_by_offset(0, 50).perform()
        webdriver.ActionChains(bot).click().perform()
        break
    except Exception:
        continue


bot.save_screenshot('clicked option ' + gettime() + '.png')

while True:
    try:
        confirm = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/button')
        confirm.click()
        break
    except Exception:
        continue

bot.save_screenshot('confirmed ' + gettime() + '.png')

