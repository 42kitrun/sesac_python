# /opt/anaconda3/envs/py310_sesac/bin/python -m pip install beautifulsoup4
# /opt/anaconda3/envs/py310_sesac/bin/python -m pip install bs4

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
import requests
from bs4 import BeautifulSoup # 안에 라이브러리 안에있는 특정 객체만 가져오기

response = requests.get('http://makemyproject.net')
print(response)
print(response.status_code)
print(response.text)

# 여기 위에는 그냥 문자열인거고
# 여기 아래는 문자를 파싱해서, DOM의 형태로 자료구조를 갖추고 있음

# HTML을 파싱해주는 라이브러리
soup = BeautifulSoup(response.text,"html.parser")
print(soup)
head = soup.find("head")
print('헤드DOM은:',head)

body = soup.find('body')
print('바디DOM은:', body)

bodytext = body.text.strip() # 문자열 가져와서 불필요한 공백 제거
print('바디내용은:', bodytext)