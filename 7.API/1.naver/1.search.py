from dotenv import load_dotenv
import urllib.request
import os

load_dotenv()  # .env 파일을 읽어서, 거기 있는 내용을 메모리에 둠

client_id = os.getenv("NAVER_CLIENT_ID") # 여기에 발급반은 ID/Secret을 입력
client_secret = os.getenv("NAVER_CLIENT_SECRET")

text = "Python 개발"

encText = urllib.parse.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))