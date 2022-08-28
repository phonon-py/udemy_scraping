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
        <li><span>Python</span>ライブラリの基礎</li>
        <span>spanテスト</span>
    </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')

# print(soup.find(id='step2').find_all('li'))
# print(soup.select('#step2 li'))
# print(soup.select('#step2 > li'))

# print(soup.select('#step2 span'))
# print(soup.select('#step2 > span'))

print(soup.select('#step2 > li > span'))
