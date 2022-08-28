from bs4 import BeautifulSoup
import requests

url = 'https://www.anaconda.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
# print(soup.find('span', id='getStartedButton').text)

# print(soup.find('h2', class_='pl-1').text)
# print(soup.find('h2', class_='mb-1').text)

# print(soup.find_all('h2', class_='mb-1'))
# for h2 in soup.find_all('h2', class_='mb-1'):
#     print(h2.text)

# print(soup.find_all('h2', class_='mb-1')[1].text)
