from bs4 import BeautifulSoup



html = '''
<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1", class="study-list">
        <li class="python-list">Python演習</li>
        <li class="html-list" value="3">html基礎</li>
        <li class="js-list">JS基礎</li>
        <li class="python-list2" value="10">Pythonライブラリ基礎</li>
        <li class="html-js-list">フロントエンド基礎</li>
    </ol>    
</body>
'''
soup = BeautifulSoup(html, 'lxml')


# print(soup.find_all('li', attrs={'value':'10'}))
print(soup.select('li:-soup-contains("Python")'))