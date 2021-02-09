from selenium import webdriver
from time import sleep

bot = webdriver.Firefox()

sleep(1)

bot.get('https://www.chess.com/home')

email = bot.find_element_by_xpath('//*[@id="username"]')

email.send_keys('MiniMaxer')

passw = bot.find_element_by_xpath('//*[@id="password"]')

passw.send_keys('HPziac9W4JRiwkE')

signin = bot.find_element_by_xpath('//*[@id="login"]')

signin.click()

exitad = bot.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div[2]/div[2]/span')

exitad.click()

bot.get('https://www.chess.com/play/computer')

#puzzles = bot.find_element_by_xpath('/html/body/div[1]/div[1]/div[11]/div[2]/a[4]')
#
#puzzles.click()

start = bot.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/button')

start.click()

start.click()

e2 = bot.find_element_by_xpath('/html/body/div[2]/chess-board/div[13]')

webdriver.ActionChains(bot).drag_and_drop_by_offset(e2, 0, -150).perform()
sleep(5)
g1 = bot.find_element_by_xpath('/html/body/div[2]/chess-board/div[10]')

webdriver.ActionChains(bot).drag_and_drop_by_offset(g1, -75, -150).perform()
