from bs4 import BeautifulSoup
import requests


url = 'https://www.python.org/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='medium-widget blog-widget')

for i,li in enumerate(post.find_all('li')):
    print('=' * 30, i, '=' *30)
    print(li.find('a').text)
    print(li.find('time').text)