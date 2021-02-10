file = open("html.txt")

html = file.read()

def slicer(str, sub):
    index = str.rfind(sub)
    if str.find('square-') == -1:
        return "cap"
    str = str[index+7:index+19]
    str = str.replace("square-", "")
    return str

def parse(html):
    substr = '"></div><div class="'
    pieces = html.split(substr)
    width = html[html.find("padding-bottom")-7: html.find("padding-bottom")-4]
    print(width)
    while pieces[-1].find('square-') == -1:
        del pieces[-1]
    for i in range(0, len(pieces)):
        pieces[i] = slicer(pieces[i], '\"piece ')
        print(pieces[i][:30])
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


parse(html)
