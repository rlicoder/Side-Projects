from selenium import webdriver
from time import sleep
import sys
from selenium.webdriver.support.ui import Select
import selenium.common.exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bot = webdriver.Firefox()
bot.set_window_size(1600, 1000)

sleeptime = int(sys.argv[1])

bot.get('https://v2.waitwhile.com/welcome/microcentertust')
sleep(sleeptime)

while True:
    try:
        WebDriverWait(bot, 100).until(EC.visibility_of(bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')))
        html = bot.page_source
        if html.find('Waitlist is currently closed') != -1:
            bot.refresh()
        else:
            break
    except Exception as e:
        print(e)

join = bot.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')

join.click()

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


while True:
    try:
        next_button = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-partysize/div/section/div[2]/div[2]/button')
        next_button.click()
        break
    except (ex.ElementClickInterceptedException, ex.NoSuchElementException) as e:
        continue;

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

drop = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/div')
drop.click()

webdriver.ActionChains(bot).move_to_element(drop).perform()
webdriver.ActionChains(bot).move_by_offset(0, 50).perform()
webdriver.ActionChains(bot).click().perform()

confirm = bot.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div[2]/div[2]/form/div[1]/button')
confirm.click()

