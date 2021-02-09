from selenium import webdriver
from time import sleep
from stockfish import Stockfish

stockfish = Stockfish('/home/royce/Desktop/Side-Projects/Chess Bot Test/stockfish')

bot = webdriver.Firefox()

sleep(1)

bot.get('https://www.chess.com/home')

email = bot.find_element_by_xpath('//*[@id="username"]')

email.send_keys('MiniMaxer')

passw = bot.find_element_by_xpath('//*[@id="password"]')

passw.send_keys('HPziac9W4JRiwkE')

signin = bot.find_element_by_xpath('//*[@id="login"]')

signin.click()

def slicer(str, sub):
    index = str.find(sub)
    str = str[index+6:index+18]
    str = str.replace("square-", "")
    return str

def parse():
    html = bot.page_source
    substr = '"></div><div class="'
    pieces = html.split(substr)
    while pieces[-1].find('square-') == -1:
        del pieces[-1]
    for i in range(0, len(pieces)):
        pieces[i] = slicer(pieces[i], 'piece ')
    rows, cols = (8, 8)
    board=[]
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(' ')
        board.append(col)

    for i in range(0, len(pieces)):
        if pieces[i].find('new') != -1:
            continue
        print(pieces[i])
        if pieces[i][0].isalpha():
            y = int(pieces[i][3])
            x = int(pieces[i][4])
            p = pieces[i][1]
            if pieces[i][0] == 'w':
                p = p.upper()
        else:
            y = int(pieces[i][0])
            x = int(pieces[i][1])
            p = pieces[i][4];
            if pieces[i][3] == 'w':
                p = p.upper()
        board[x-1][y-1] = p;

    FEN = ""

    for i in range(7,-1, -1):
        count = 0
        for j in range(0,8):
            if board[i][j] == ' ':
                count += 1
            else:
                if count > 0:
                    FEN += (str(count))
                    count = 0
                FEN += (board[i][j])
        if count > 0:
            FEN += (str(count))
        FEN += ('/')

    FEN += " w - - 0 0"
    return FEN


while (True):
    answer = str(input("Go?"))
    if answer == 'y':
        FEN = parse()
        stockfish.set_fen_position(FEN)
        move = stockfish.get_best_move()
        print(stockfish.get_evaluation())
        print(move)
        posx = int(move[1])
        posy = int(ord(move[0]) - 96)
        search = "square-"
        search += str(posy)
        search += str(posx)
        print(search)
        piecel = bot.find_elements_by_class_name(search);
        if len(piecel) == 2:
            piece = piecel[1]
        else:
            piece = piecel[0]
        endx = int(move[3])
        endy = int(ord(move[2]) - 96)
        difx = endx - posx
        dify = endy - posy
        print("processing move")
        webdriver.ActionChains(bot).drag_and_drop_by_offset(piece, dify * 75, difx * -75).perform()
        print("done")
        print(stockfish.get_board_visual())
    else:
        break

