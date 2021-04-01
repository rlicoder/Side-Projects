from bs4 import BeautifulSoup as bs
import re
import urllib.request
import unicodedata


cities = ['riverside']

for j in cities:
    for k in range(0, 200, 10):
        url = 'https://www.yelp.com/search?find_desc=&find_loc='
        url += j
        url += '%2C%20CA&ns=1&start='
        print(j + ' ' + str(k))
        url += str(k)

        yelp = urllib.request.urlopen(url)

        soup = bs(yelp, 'html.parser')

        table = soup.find_all('div', class_= re.compile('^scrollablePhotos'))

        f = open('places.txt', 'a', encoding='utf-8')
        d = open('debug.txt', 'a', encoding='utf-8')
        for i in range(0, len(table)):
            if i == 0:
                continue
            if table[i] is None:
                continue
            if table[i].get_text().find('$') == -1:
                continue
            raw_title = re.search('\D+?(?=\d)', table[i].get_text())
            if raw_title is None:
                continue
            raw_title_text = unicodedata.normalize('NFKD', raw_title.group())
            raw_phone = re.search('\(\d{3}\) \d{3}-\d{4}', table[i].get_text())
            if raw_phone is None:
                continue
            address = re.search('\d+\D+$', table[i].get_text().replace(raw_phone.group(), '')).group()
            if address is None:
                continue
            title = re.sub('\d*?\. ', '', raw_title_text)
            phone = re.sub('\D', '', raw_phone.group())
            if not title or len(title) == 0:
                continue
            if not phone or len(phone) == 0:
                continue
            if not address or len(address) == 0:
                continue
            f.write(str(title))
            f.write('\n')
            f.write(str(phone))
            f.write('\n')
            f.write(str(address))
            f.write('\n\n')


