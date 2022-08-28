from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

# print(post.find('li').find('a').attrs['href'])
# print(post.find('li').find('a')['href'])
# print(post.find('li').find('a').get('href'))

# print(post.parent)

# print(post.find('ul').contents)
# for tag in post.find('ul').contents:
#     print(tag)
