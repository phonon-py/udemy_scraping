from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

search_box = driver.find_element_by_css_selector('input.sc-TOsTZ')
sleep(3)

search_box.send_keys('Python')
sleep(5)

text = search_box.get_attribute('value')
search_box.send_keys(Keys.BACKSPACE * len(text))
# search_box.clear()
sleep(5)

search_box.send_keys('機械学習')
sleep(5)

search_box.submit()
sleep(3)

driver.quit()
