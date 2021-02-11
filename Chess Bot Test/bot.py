from selenium import webdriver
from time import sleep
from stockfish import Stockfish
from parse import *

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

while (True):
    answer = str(input("Go?"))
    if answer == 'q':
        break
    else:
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

bot.quit()
