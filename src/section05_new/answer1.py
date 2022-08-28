from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = 'https://employment.en-japan.com'
url = 'https://employment.en-japan.com/wish/search_list/?companytype=0&worktype=0&areaid=23_24_21_50&occupation=101000_102500_103000_103500_104500_105000_105500_109000&indexNoWishArea=0&sort=wish'

r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.content, 'lxml')

jobs = soup.find_all('div', class_='jobNameArea')
print(len(jobs))

d_list = []

for job in jobs[:2]:
    company_name = job.find('span', class_='company').text
    page_url = base_url + job.find('a').get('href')

    if 'fromSearch' in page_url:
        path = page_url.replace(base_url+'/desc_eng_', '')
        e_index = path.rfind('/')

        company_id = path[:e_index]
        print(f'fromSearchが含まれるURLのカンパニーIDは{company_id}です')

        page_url = f'https://en-gage.net/recruit/?getFromEmploy={company_id}'
        print(f'fromSearchの含まれるサイトURLは{page_url}になります。')

    sleep(3)
    page_r = requests.get(page_url)
    page_r.raise_for_status()

    page_soup = BeautifulSoup(page_r.content, 'lxml')

    company_url = None

    if 'PK' in page_url:
        company_info_block = [h2_tag for h2_tag in page_soup.find_all('h2', class_="text") if '会社概要' in h2_tag.text][0]
        company_summary = company_info_block.parent.parent

        for table_row in company_summary.find_all('tr'):
            if table_row.find('th').text == '企業ホームページ':
                company_url = table_row.find('td').find('a').text
    
    elif 'getFromEmploy' in page_url:
        company_summary = page_soup.find('table', class_='companyTable')

        for table_row in company_summary.find_all('tr'):
            if '企業WEBサイト' in table_row.find('th').text:
                company_url = table_row.find('td').find('a').get('href')

    else:
        raise       
    
    d_list.append({
        'company_name': company_name,
        'company_url': company_url
    })
    print(d_list[-1])

    
df = pd.DataFrame(d_list)
# df.to_csv('enjapan_company_list.csv', index=False, encoding='utf-8-sig')