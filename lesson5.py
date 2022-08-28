import re

from bs4 import BeautifulSoup
import requests


url = 'https://www.python.org/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='medium-widget blog-widget')

print(soup.find(href='/about/'))