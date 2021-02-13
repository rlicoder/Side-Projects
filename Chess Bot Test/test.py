import re
file= open('html.txt', 'r')
html = file.read()
pat = re.findall('data-whole-move-number="\d*?"(?!.*data-whole-move-number)', html)
print(pat[0])
for i in pat:
    print(i)
