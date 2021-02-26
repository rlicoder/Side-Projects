from selenium import webdriver
from time import sleep
from stockfish import Stockfish
from parse import *
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

def runbot():
    settings = open("settings.txt", "r")
    thr = settings.readline()
    mintime = settings.readline()
    level = settings.readline()
    mindep = settings.readline()
    hashsize = settings.readline()
    con = settings.readline()
    slow = settings.readline()
    timecons = settings.readline()
    delayon = bool(settings.readline())
    beg_delay = int(settings.readline())
    mid_delay = int(settings.readline())
    end_delay = int(settings.readline())
    settings.close()

    stockfish = Stockfish('/home/royce/Desktop/Side-Projects/Chess Bot Test/stockfish', parameters={"Threads": thr, "Minimum Thinking Time": mintime, "Skill Level": level, "Min Split Depth": mindep, "Hash": hashsize, "Contempt": con, "Slow Mover": slow})

    bot = webdriver.Firefox()


    sleep(1)

    bot.get('https://www.chess.com/home')
    email = bot.find_element_by_xpath('//*[@id="username"]')
    email.send_keys('MiniMaxer')
    passw = bot.find_element_by_xpath('//*[@id="password"]')
    passw.send_keys('HPziac9W4JRiwkE')
    signin = bot.find_element_by_xpath('//*[@id="login"]')
    signin.click()

    time = input("time control?")
    cont = "New " + time + " min"
    print(cont)

    while (cont != 'q'):
        html = bot.page_source
        while (html.find(cont)) == -1:
            sleep(.5)
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
            if delayon:
                if turnnum <= 10:
                    offset = random.randint(0,beg_delay)
                    timecons = 20
                elif turnnum >= 10 and turnnum <= 30:
                    offset = random.randint(0,mid_delay)
                    timecons = 500
                elif turnnum >= 31 and turnnum <=50:
                    offset = random.randint(0,end_delay)
                    timecons = 250
                    stockfish.set_depth(7)
                else:
                    offset = 0
                    timecons = 50
                    stockfish.set_depth(18)
                sleep(offset/1000)
            FEN, dirx, diry = parse(bot)
            stockfish.set_fen_position(FEN)
            move = stockfish.get_best_move_time(timecons)
            print(move)
            print(stockfish.get_evaluation())
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
        try:
            nextb = bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[5]/div[1]/button[2]')
        except NoSuchElementException:
            nextb = bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[4]/div[1]/button[2]')
        html = bot.page_source
        nextb.click()
        sleep(3)
        while (html.find('Draw') == -1):
            html = bot.page_source
            try:
                nextb.click()
                sleep(.1)
                nextb.click()
            except StaleElementReferenceException:
                break
            except StaleElementException:
                break       
            sleep(10)
    bot.quit()
    stockfish.stockfish
