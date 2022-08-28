import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

# for text in soup.find_all('a', text=re.compile('Python')):
#     print(text)


for text in soup.find_all('a', href=re.compile('docs.python.org')):
    print(text)
