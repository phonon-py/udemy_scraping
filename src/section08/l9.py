from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)

driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

# e = driver.find_element_by_id('uamods-topics')
# print(e)
# print(e.text)

# e = driver.find_element_by_class_name('sc-kfGgVZ')
# print(e)
# print(e.text)

a_tags = driver.find_elements_by_class_name('sc-esjQYD')

for a_tag in a_tags:
    print(a_tag.text)
    print(a_tag.get_attribute('href'))

driver.quit()
