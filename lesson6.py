import re

from bs4 import BeautifulSoup
import requests


url = 'https://www.python.org/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='medium-widget blog-widget')

# Pythonとはいっている要素全てを取得する
for text in soup.find_all('a', href=re.compile('docs.python.org')):
    print(text)
