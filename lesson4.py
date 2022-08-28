from bs4 import BeautifulSoup
import requests


url = 'https://www.python.org/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='medium-widget blog-widget')

# print(post.find('li').find('a')['href'])
# print(post.find('li').find('a').get('href'))

# print(post.parent)
for i,tag in enumerate(post.find('ul').contents):
    print(i,tag)