from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)

driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

e = driver.find_element_by_tag_name('h2')
# print(e.text)
# print(e.get_attribute('outerHTML'))

h2_tags = driver.find_elements_by_tag_name('h2')

for h2_tag in h2_tags:
    print(h2_tag.text)
    print(h2_tag.get_attribute('outerHTML'))

driver.quit()
