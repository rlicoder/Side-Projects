from selenium import webdriver
from time import sleep

bot = webdriver.Firefox()

bot.get('https://v2.waitwhile.com/welcome/microcentertust')
#set sleep for browser to initially load the page (in secs)
sleep(3)

html = bot.page_source

f = open('debug.txt', 'w')

while (html.find('Waitlist is currently closed') != -1):
    bot.refresh()
    #set sleep for browser to refresh the page (in secs)
    sleep(3)
    html = bot.page_source
    f.write(html)

f.close()

for i in range(0, 100):
    print('\a')
    sleep(1)




