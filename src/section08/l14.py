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

search_box = driver.find_element_by_css_selector('input.sc-TOsTZ')
sleep(3)

search_box.send_keys('機械学習')
sleep(3)

search_box.submit()
sleep(3)


while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)

    button = driver.find_elements_by_css_selector(
        'div.newsFeed > div > span > button')
    sleep(2)

    if button:
        button[0].click()
    else:
        break


a_tags = driver.find_elements_by_css_selector('a.newsFeed_item_link')

for i, a_tag in enumerate(a_tags):
    print('='*30, i, '='*30)
    print(a_tag.find_element_by_css_selector('.newsFeed_item_title').text)
    print(a_tag.get_attribute('href'))


driver.quit()
