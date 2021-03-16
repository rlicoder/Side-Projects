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

        f = open ('places.txt', 'a')
        #print(url)
        for i in range(0, len(table)):
            if i == 0:
                continue
            if (table[i] is None):
                continue
            raw_title = re.search('\D+?(?=\d)', table[i].get_text())
            if raw_title is None:
                continue
            raw_title_text = unicodedata.normalize('NFKD', raw_title.group())
            title = re.sub('(\d+?|)\. ', '', raw_title_text)
            raw_phone = re.search('\(\d{3}\) \d{3}-\d{4}', table[i].get_text())
            if raw_phone is None:
                continue
            phone = re.sub('\D', '', raw_phone.group())
            if not title:
                continue
            if not phone:
                continue
            f.write(title)
            f.write('\n')
            f.write(phone)
            f.write('\n')


