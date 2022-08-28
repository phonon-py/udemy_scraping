from bs4 import BeautifulSoup

html = """
<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1", class="study-list">
        <li>Python基礎</li>
        <li>HTML基礎</li>
        <li>JS基礎</li>
        <li>Pythonライブラリの基礎</li>
    </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')

# print(soup.select_one('li:first-of-type'))
# print(soup.select_one('li:last-of-type'))

# print(soup.select_one('li:nth-of-type(3)'))

print(soup.select_one('li:first-of-type') ==
      soup.select_one('li:nth-of-type(1)'))
