from time import sleep
from selenium import webdriver


# STEP1 : Driverの作成
driver = webdriver.Chrome(executable_path='')

# STEP2 : driver.get()でサイトにアクセスする
driver.get('https://www.google.co.jp')
sleep(3)

# STEP3 : 要素を取得して何らかの処理をする
search_bar = driver.find_element_by_name('q')
sleep(3)

search_bar.send_keys('python')
sleep(3)

search_bar.submit()
sleep(5)

driver.quit()
