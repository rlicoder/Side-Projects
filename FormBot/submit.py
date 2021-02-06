from selenium import webdriver
from time import sleep
import random

first = [];
last = [];
messages = [];
emails = [];
with open("LastNames.txt") as file:
    for name in file:
        name.strip()
        last.append(name)

with open("FirstNames.txt") as file:
    for name in file:
        name.strip();
        first.append(name)

with open("Emails.txt") as file:
    for email in file:
        email.strip();
        emails.append(email)

with open("Messages.txt") as file:
    for msg in file:
        msg.strip();
        messages.append(msg)

bot = webdriver.Firefox();

url_file = open("url.txt")

url = url_file.readline();

bot.get(url)

sleep(2);

cards = [];

with open("xpathcards.txt") as file:
    for path in file:
        cards.append(path)

fname = bot.find_element_by_xpath('//*[@id="cons_first_name"]')
lname = bot.find_element_by_xpath('//*[@id="cons_last_name"]')
ebox = bot.find_element_by_xpath('//*[@id="cons_email"]')
mbox = bot.find_element_by_xpath('//*[@id="2655_3100_5_3484"]')
card = bot.find_element_by_xpath(cards[random.randint(0,len(cards)-1)])
submit = bot.find_element_by_xpath('//*[@id="ACTION_SUBMIT_SURVEY_RESPONSE"]')

randf = random.randint(0, len(first)-1)
randl = random.randint(0, len(last)-1)
randm = random.randint(0, len(messages)-1)
rande = random.randint(0, len(emails)-1)

card.click();
fname.send_keys(first[randf])
lname.send_keys(last[randl])
ebox.send_keys(emails[rande])
mbox.send_keys(messages[randm])
submit.click()
bot.quit()
