from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

print(soup.find(text='Latest News').parent)
print(soup.find(href='/about/'))
