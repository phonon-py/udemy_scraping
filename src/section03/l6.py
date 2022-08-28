from bs4 import BeautifulSoup
import requests

url = 'https://www.anaconda.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
# print(soup.find(attrs={'data-barba': 'container'}))

print(soup.find_all('h2', class_='mb-1'))
print(soup.find_all('h2', attrs={'class': 'mb-1'}))
