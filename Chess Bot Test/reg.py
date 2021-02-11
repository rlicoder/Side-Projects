import re

f = open("html.txt", "r")
html = f.read()

pattern = re.compile('width: \d\d\dpx')

matches = pattern.finditer(html)

for i in matches:
    print(i)
