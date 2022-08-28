from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--incognito')
# options.add_argument(
#     '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)

driver.get('https://www.google.co.jp')
# driver.get('https://testpage.jp/tool/ip_user_agent.php')
sleep(3)

driver.quit()
