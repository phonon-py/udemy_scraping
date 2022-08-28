from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

d_list = []
for li in post.find_all('li'):
    d = {
        'title': li.find('a').text,
        'url': li.find('a').get('href'),
        'date': li.find('time').text
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
print(df)

df.to_csv('python_web_posts.csv', index=None, encoding='utf-8-sig')
# df.to_excel('python_web_posts.xlsx', index=None, encoding='utf-8-sig')
