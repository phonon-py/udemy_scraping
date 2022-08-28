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

# driver.execute_script('window.scrollTo(0, 500);')
# sleep(5)

# height = 500
# while height < 3000:
#     driver.execute_script(f'window.scrollTo(0, {height});')
#     height += 100
#     sleep(1)


height = driver.execute_script("return document.body.scrollHeight")
sleep(3)

driver.execute_script(f'window.scrollTo(0, {height});')
sleep(3)


driver.quit()
