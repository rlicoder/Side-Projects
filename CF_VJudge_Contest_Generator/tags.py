from bs4 import BeautifulSoup as bs
import re
import urllib.request

codeforces = urllib.request.urlopen("https://codeforces.com/problemset/")
soup = bs(codeforces, 'html.parser')

max_page = 1
for i in (soup.find_all(class_='page-index')):
    max_page = max(int(i.get_text()), max_page)

x = set()
for l in range(1, max_page+1): 
    print(float(l/max_page) * 100, end='%\n')
    url = "https://codeforces.com/problemset/page/"
    url += str(l)
    codeforces = urllib.request.urlopen(url)
    soup = bs(codeforces, 'html.parser')
    table = soup.find('table', class_='problems').find_all('tr')
    for i in range(1, len(table)):
        for j in table[i].find_all('td'):
            if (len(j.find_all('div')) == 2):
                for k in range(0, len(j.find_all('div'))):
                    if (k == 1):
                        tags = re.sub('\s+', ' ', j.find_all('div')[k].get_text().strip().replace('\r\n', ' ').replace('"', '')).split(',')
                        for m in tags:
                            x.add(m.strip())

for i in x:
    print(i)

