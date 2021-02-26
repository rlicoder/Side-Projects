from selenium import webdriver
from time import sleep

f = open('debug.txt', 'w')

bot = webdriver.Firefox()

sleeptime = int(input("how many seconds in between loading pages?"))

bot.get('https://v2.waitwhile.com/welcome/microcentertust')
sleep(sleeptime)

html = bot.page_source

while (html.find('Waitlist is currently closed') != -1):
    while (html.find('Waitlist is currently closed') != -1):
        bot.refresh()
        sleep(sleeptime)
        html = bot.page_source
    bot.quit()
    bot.get('https://v2.waitwhile.com/welcome/microcentertust')
    bot.refresh()
    sleep(sleeptime)
    html = bot.page_source

f.write(html)
f.close()

for i in range(0, 100):
    print('\a')
    sleep(1)




