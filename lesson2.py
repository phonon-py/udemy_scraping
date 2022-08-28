import requests
from bs4 import BeautifulSoup


url = 'https://www.anaconda.com/'
r = requests.get(url)


soup = BeautifulSoup(r.content, 'lxml')
print(soup.h1.text)
print('####')
print(soup.find('h1').text)
print('####')
print(soup.find('span',class_='btn js-getStarted-button').text)
print(soup.find_all('span',class_='green')[1].text)
print('####')

for i,h2 in enumerate(soup.find_all('h2',class_='mb-1')):
    print(i,h2.text)

print('####')
print(soup.find(attrs={'data-barba':'container'}))