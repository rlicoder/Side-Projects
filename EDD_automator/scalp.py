from bs4 import BeautifulSoup as bs
import re
import urllib.request

yelp = urllib.request.urlopen('https://www.yelp.com/search?find_desc=&find_loc=Corona%2C+CA&ns=1')

soup = bs(yelp, 'html.parser')

print(soup)
table = soup.find_all('div')

print(len(table))
for i in table:
    print(i.get_text())


