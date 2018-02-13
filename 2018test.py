import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('https://iluvpitunia.github.io/')
# HTML 소스 가져오기
html = req.text
# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select('#main > article > div > div > ul > li > article > a > span.excerpt')

#data = {}

#for title in my_titles:
#    data[title.text] = title.get('href')

#with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#    json.dump(data, json_file)
    
for title in my_titles:
    # Tag안의 텍스트
    print(title.text + "\n" )

