import chess
import chess.engine
from rpiengine import getMove
import logging
from selenium import webdriver
from time import sleep
from parse import *
import random
from selenium.common.exceptions import *
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import StaleElementReferenceException
logging.basicConfig(format='%(asctime)s %(lineno)d %(message)s')

bot = webdriver.Chrome()
bot.set_page_load_timeout(20)

logging.debug('Logging in to Chess.com'_)
bot.get('https://www.chess.com/home')
email = bot.find_element_by_xpath('//*[@id="username"]')
email.send_keys('MiniMaxer')
passw = bot.find_element_by_xpath('//*[@id="password"]')
passw.send_keys('HPziac9W4JRiwkE')
signin = bot.find_element_by_xpath('//*[@id="login"]')
signin.click()
logging.debug('Logged in')

logging.debug('Getting time controls')
time = input("time control?")
cont = "New " + time + " min"
logging.debug('Time controls set to: %s', cont)

while (cont != 'q'):
    logging.debug('Fetching html')
    html = bot.page_source
    logging.debug('Fetched')
    while (html.find(cont)) == -1:
        html = bot.page_source
        if html.find('<text x="10" y="99" font-size="2.8" class="coordinate-dark">h</text>') != -1:
            look = "black"
        else:
            look = "white"
        loc = html.find('clock-player-turn')
        turn = html[loc-130:loc]
        while turn.find(look) == -1:
            html = bot.page_source
            if (html.find(cont)) != -1:
                break
            loc = html.find('clock-player-turn')
            turn = html[loc-130:loc]
        if html.find(cont) != -1:
            break
        html = bot.page_source
        pat = re.findall('data-whole-move-number="\d*?"(?!.*data-whole-move-number)', html)
        if len(pat) == 0:
            turnnum = 0
        else:
            pat[0] = pat[0].replace('data-whole-move-number="', '')
            pat[0] = pat[0].replace('"', '')
            turnnum = int(pat[0])
        if turnnum <= 10:
            time = .1
        elif turnnum > 10 and turnnum < 30:
            time = random.randint(0,5)
        else:
            time = .1
        logggin.debug('Turn #%d, Delay:%d', turnnum, time)
        FEN, dirx, diry = parse(bot)
        logging.debug('Fen: %s, x_dir: %d, y_dir: %d', FEN, dirx, diry)
        move = str(getMove(FEN, time))
        logging.debug('Chosen Move: %s', move)
        posx = int(move[1])
        posy = int(ord(move[0]) - 96)
        search = "square-"
        search += str(posy)
        search += str(posx)
        piecel = bot.find_elements_by_class_name(search);
        if len(piecel) == 2:
            piece = piecel[1]
        else:
            piece = piecel[0]
        endx = int(move[3])
        endy = int(ord(move[2]) - 96)
        difx = endx - posx
        dify = endy - posy
        webdriver.ActionChains(bot).drag_and_drop_by_offset(piece, dify * diry, difx * dirx).perform()
        html = bot.page_source
    sleep(random.randint(0,500)/1000)
    buttontext = '//button[normalize-space()="'
    buttontext += cont
    buttontext += "]"
    nextb = bot.find_element_by_xpath(buttontext)
    html = bot.page_source
    sleep(1)
    logging.debug('Next match clicked')
    nextb.click()
    sleep(1)
    while (html.find('Draw') == -1):
        html = bot.page_source
        try:
            sleep(.5)
            nextb.click()
            sleep(.5)
            nextb.click()
            logging.debug('Clicked twice')
        except StaleElementReferenceException:
            break
        except StaleElementException:
            break       
        sleep(10)
bot.quit()


