from bs4 import BeautifulSoup as bs
import re
import urllib.request

codeforces = urllib.request.urlopen("https://codeforces.com/problemset/")

soup = bs(codeforces, 'html.parser')

max_page = 1
for i in (soup.find_all(class_='page-index')):
    max_page = max(int(i.get_text()), max_page)

codeforces = urllib.request.urlopen("https://codeforces.com/problemset/page/1")

soup = bs(codeforces, 'html.parser')

f = open('test.csv', 'w')
for l in range(0, max_page+1): 
    print(float(l/max_page) * 100, end='%\n')
    url = "https://codeforces.com/problemset/page/"
    url += str(l)
    codeforces = urllib.request.urlopen(url)
    soup = bs(codeforces, 'html.parser')
    table = soup.find('table', class_='problems').find_all('tr')
    for i in range(1, len(table)):
        for j in table[i].find_all('td'):
            if (len(j.find_all('div')) == 2):
                for k in j.find_all('div'):
                    #print(re.sub('\s+', ' ', k.get_text().strip().replace('\r\n', ' ').replace(',', ' ').replace('"', '')))
                    f.write(re.sub('\s+', ' ', k.get_text().strip().replace('\r\n', ' ').replace(',', ' ').replace('"', '')))
                    f.write(', ')
            else:
                #print(j.get_text().strip())
                f.write(j.get_text().strip())
                f.write(', ')
        f.write('\n')
f.close()
