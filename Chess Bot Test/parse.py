file = open("html.txt")

html = file.read()

substr = '"></div><div class="'

pieces = html.split(substr)
del pieces[-1]
del pieces[-1]

def slicer(str, sub):
    index = str.find(sub)
    return str[index+6:index+18]

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
    p = pieces[i][1]
    if pieces[i][0] == 'w':
        p = p.upper();
    x = int(pieces[i][-1])
    y = int(pieces[i][-2])
    board[x-1][y-1] = p;

FEN = ""

for i in range(7,0, -1):
    count = 0
    for j in range(0,8):
        if (board[i][j] == ' '):
            count += 1
        else:
            if count > 0:
                FEN += (str(count))
                count = 0
            FEN += (board[i][j])
    if count > 0:
        FEN += (str(count))
    FEN += ('/')

print(FEN)

