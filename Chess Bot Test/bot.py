from selenium import webdriver
from time import sleep
from stockfish import Stockfish
from parse import *
import random

settings = open("settings.txt", "r")
thr = settings.readline()
mintime = settings.readline()
level = settings.readline()
mindep = settings.readline()
hashsize = settings.readline()
con = settings.readline()
slow = settings.readline()
timecons = settings.readline()
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

go = input("go?")

while (True):
    html = bot.page_source

    while (html.find('New 3 Min')) == -1:
        html = bot.page_source
        if html.find('<text x="10" y="99" font-size="2.8" class="coordinate-dark">h</text>') != -1:
            look = "black"
        else:
            look = "white"
        loc = html.find('clock-player-turn')
        turn = html[loc-130:loc]
        while turn.find(look) == -1:
            html = bot.page_source
            loc = html.find('clock-player-turn')
            turn = html[loc-130:loc]
        re.compile('data-whole-move-number="\d*?"(?!.*data-whole-move-number)')
        lastmove = html.rfind('data-whole-move-number=')
        turnnum = int(html[lastmove+20:lastmove+27])
        print(turnnum)
        if turnnum <= 10:
            offset = random.randint(0,300)
        elif turnnum >= 10 and turnnum <= 40:
            offset = random.randint(1000,5000)
        else:
            offset = random.randint(0,100)
        sleep(offset/1000)
        FEN, dirx, diry = parse(bot)
        stockfish.set_fen_position(FEN)
        move = stockfish.get_best_move_time(timecons)
        print(stockfish.get_evaluation())
        print(move)
        print(stockfish.get_board_visual())
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
        sleep(1)
    next = bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[4]/div[1]/button[2]')
    next.click()


bot.quit()
