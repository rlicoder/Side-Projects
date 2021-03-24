from selenium import webdriver
from time import sleep


bot = webdriver.Firefox()
bot.set_page_load_timeout(10)
f = open('places.txt', 'r')
name = f.readline()

bot.get('https://www.html.am/html-codes/textboxes/html-textbox.cfm')

while name:
    bot.find_element_by_xpath('/html/body/div[1]/article/table[1]/tbody/tr[2]/td[1]/textarea').send_keys(name)
    name = f.readline()

sleep(10000)
ini.click()

table = bot.find_element_by_class_name('ui-datepicker-calendar')

rows = table.find_elements_by_tag_name('tr')

for i in rows:
    cols = i.find_elements_by_tag_name('td')
    for j in cols:
        print(j.text)
        print(j.get_attribute('class'))
