from bs4 import BeautifulSoup

html = """
<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1", class="study-list">
        <li>Python基礎</li>
        <li>HTML基礎</li>
    </ol>
    <ol id="step2" class="study-list">
        <li>JS基礎</li>
        <li>Pythonライブラリの基礎</li>
    </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.find('h2').text)
# print(soup.select_one('h2').text)

# print(soup.find(id='step1').text)
# print(soup.select_one('#step1').text)

# print(soup.find(class_='study-list').text)
# print(soup.select_one('.study-list').text)

# print(soup.find_all(class_='study-list'))
# print(soup.select('.study-list'))
