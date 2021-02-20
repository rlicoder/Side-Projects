from selenium import webdriver
from time import sleep
import urllib.request
import re
import requests

html = requests.get('https://twitch.tv/gmhikaru').content
f = open('html.txt','w')
f.write(str(html))
f.close()
print(str(html).find('LIVE'))
