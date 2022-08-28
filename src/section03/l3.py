from bs4 import BeautifulSoup
import requests

url = 'https://www.anaconda.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.h1.text)
