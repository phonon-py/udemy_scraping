from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
# options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)

driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

a_tag = driver.find_element_by_css_selector(
    'div.sc-jgVwMx > div > ul > li:nth-of-type(3) > a')
sleep(3)

a_tag.click()
sleep(5)

driver.quit()
