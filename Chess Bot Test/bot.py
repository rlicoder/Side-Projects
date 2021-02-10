from selenium import webdriver
from time import sleep
from stockfish import Stockfish

stockfish = Stockfish('/home/royce/Desktop/Side-Projects/Chess Bot Test/stockfish', parameters={"Threads": 6, "Minimum Thinking Time": 750, "Skill Level": 20, "Min Split Depth": 10, "Hash": 2048, "Contempt": 50, "Slow Mover": 120})

bot = webdriver.Firefox()

sleep(1)

bot.get('https://www.chess.com/home')
email = bot.find_element_by_xpath('//*[@id="username"]')
email.send_keys('MiniMaxer')
passw = bot.find_element_by_xpath('//*[@id="password"]')
passw.send_keys('HPziac9W4JRiwkE')
signin = bot.find_element_by_xpath('//*[@id="login"]')
signin.click()

dirx = [1]
diry = [1]

def slicer(str, sub):
    index = str.rfind(sub)
    if str.find('square-') == -1:
        return "cap"
    str = str[index+7:index+19]
    str = str.replace("square-", "")
    return str

def parse(dirx, diry):
    html = bot.page_source
    if html.find('<text x="10" y="99" font-size="2.8" class="coordinate-dark">h</text>') != -1:
        dirx[0] = 75
        diry[0] = -75
    else:
        dirx[0] = -75
        diry[0] = 75
    whiteturn = True
    if html.find('clock-player-turn') != -1:
        loc = html.find('clock-player-turn')
        turn = html[loc-57:loc-47]
        if turn.find('white') != -1:
            whiteturn = True
        else:
            whiteturn = False
    elif html.find('to Move') != -1:
        if (html.find('Black to Move')) != -1:
            whiteturn = False
        else:
            whiteturn = True
    else:
        t = str(input('w or b'))
        if t == 'w':
            whiteturn = True
        else:
            whiteturn = False

    substr = '"></div><div class="'
    pieces = html.split(substr)
    while pieces[-1].find('square-') == -1:
        del pieces[-1]
    for i in range(0, len(pieces)):
        pieces[i] = slicer(pieces[i], '\"piece ')
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
        if pieces[i].find('cap') != -1:
            continue;
        #print(pieces[i])
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

    if whiteturn == True:
        FEN += " w"
    else:
        FEN += " b"
    cast = False;
    FEN += " ";
    if board[0][7] == 'R' and board[0][4] == 'K':
        FEN += "K"
        cast = True
    if board[0][0] == 'R' and board[0][4] == 'K':
        FEN += "Q"
        cast = True
    if board[7][4] == 'k' and board[7][7] == 'r':
        FEN += "k"
        cast = True
    if board[7][0] == 'r' and board[7][4] == 'k':
        FEN += "q"
        cast = True
    FEN += " "
    if cast == False:
        FEN += " - "
    FEN += " - 0 0"
    return FEN


while (True):
    answer = str(input("Go?"))
    if answer == '3':
        bot.quit()
        break
    elif answer == '2':
        FEN = parse(dirx, diry)
        stockfish.set_fen_position(FEN)
        print(stockfish.get_evaluation())
        print(stockfish.get_board_visual())
    elif answer == '1':
        FEN = parse(dirx, diry)
        stockfish.set_fen_position(FEN)
        print(FEN)
        print(stockfish.get_best_move_time(500))
        print(stockfish.get_evaluation())
        print(stockfish.get_board_visual())
    else:
        FEN = parse(dirx, diry)
        stockfish.set_fen_position(FEN)
        move = stockfish.get_best_move_time(750)
        #print(stockfish.get_evaluation())
        print(move)
        posx = int(move[1])
        posy = int(ord(move[0]) - 96)
        search = "square-"
        search += str(posy)
        search += str(posx)
        #print(search)
        piecel = bot.find_elements_by_class_name(search);
        if len(piecel) == 2:
            piece = piecel[1]
        else:
            piece = piecel[0]
        endx = int(move[3])
        endy = int(ord(move[2]) - 96)
        difx = endx - posx
        dify = endy - posy
        webdriver.ActionChains(bot).drag_and_drop_by_offset(piece, dify * diry[0], difx * dirx[0]).perform()
        #print(stockfish.get_board_visual())

