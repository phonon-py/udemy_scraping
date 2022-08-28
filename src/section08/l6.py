from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)
driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

driver.find_element_by_id('ppppppp')

driver.quit()
