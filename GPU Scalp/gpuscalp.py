from selenium import webdriver
from time import sleep
import sys

f = open('debug.txt', 'w')

bot = webdriver.Firefox()

sleeptime = int(sys.argv[1])

bot.get('https://v2.waitwhile.com/welcome/microcentertust')
sleep(sleeptime)

html = bot.page_source

while (html.find('Waitlist is currently closed') != -1):
    bot.refresh()
    sleep(sleeptime)
    html = bot.page_source
    while (html.find('Waitlist is currently closed') != -1):
        bot.refresh()
        sleep(sleeptime)
        html = bot.page_source
    bot.quit()
    bot.get('https://v2.waitwhile.com/welcome/microcentertust')
    bot.refresh()
    sleep(sleeptime+5)
    if (len(html) == 0):
        continue
    html = bot.page_source

f.write(html)
f.close()

for i in range(0, 1000):
    print('\a')
    sleep(1)




