from stockfish import Stockfish


def slicer(str, sub):
    index = str.rfind(sub)
    print(str)
    if str.find('square-') == -1:
        return "cap"
    str = str[index+7:index+19]
    str = str.replace("square-", "")
    print(str)
    return str

def parse():
    file = open("html.txt")
    html = file.read()

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
        if pieces[i].find('new') != -1 and pieces[i].find('wr') == -1:
            continue
        if pieces[i].find('cap') != -1 and pieces[i].find('wr') == -1:
            continue;
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

    print(pieces)
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

    return FEN

FEN = parse()
stockfish = Stockfish('/home/royce/Desktop/Side-Projects/Chess Bot Test/stockfish')
stockfish.set_fen_position(FEN)
print(stockfish.get_board_visual())

