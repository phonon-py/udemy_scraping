from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://employment.en-japan.com/desc_1179281/?PK=192A36&arearoute=1'

r = requests.get(url)
page_soup = BeautifulSoup(r.content, 'lxml')

company_url = None

company_info_block = [h2 for h2 in page_soup.find_all('h2', class_='text') if '会社概要' in h2.text][0]
company_summary = company_info_block.parent.parent

for table_row in company_summary.find_all('tr'):
    if table_row.find('th').text == '企業ホームページ':
        company_url = table_row.find('td').find('a').text # 納得できんけどコピペで動作した

print('#'*30)
print(company_url)