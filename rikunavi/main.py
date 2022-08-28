from os import access
from time import sleep
import random
from webbrowser import get

import requests
from bs4 import BeautifulSoup
import pandas as pd


d_list = []

# 企業のベースとなるURL
base_url = 'https://next.rikunabi.com'

# sleep秒数
sec = random.uniform(1,3)

# リクナビネクスト検索結果
# 1 : 1
# 2 : 51(+50)
# 3 : 101(+50)
urls = 'https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0100000000&wrk_plc_long_cd=0313000000&wrk_plc_long_cd=0313100000&wrk_plc_long_cd=0314000000&curnum={}'

for i in range(3):
    url = urls.format(1+50*i)

    sleep(sec)

    r = requests.get(url, timeout=3)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')


    page_urls = soup.select('a:-soup-contains(企業ページ)')

    for page_url in page_urls:
        page_url = base_url + page_url.get('href')
        print(f'企業ページ:{page_url}')

        sleep(sec)
        
        company_r = requests.get(page_url, timeout=3)
        company_r.raise_for_status()
        
        page_soup = BeautifulSoup(company_r.content, 'lxml')

        comany_name = page_soup.select_one('.rnn-breadcrumb > li:last-of-type').text
        print(f'会社名:{comany_name}')
        
        url_in_tag = page_soup.select_one('.rnn-col-11:last-of-type a')
        company_url = url_in_tag.get('href') if url_in_tag else None # 三項演算子
        print(f'企業URL:{company_url}')

        d_list.append({
            'company_name':comany_name,
            'company_url':company_url
        })
        print(d_list[-1])

df = pd.DataFrame(d_list)
df.to_csv('rikunabi_company_list.csv', index=None, encoding='utf-8-sig')