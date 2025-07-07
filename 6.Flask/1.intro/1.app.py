# pip install flask
from flask import Flask

# app = Flask('myapp1')
# app2 = Flask('myapp2')
# app3 = Flask('myapp3')

app = Flask(__name__)

@app.route('/') # 사용자가 /에 접속하면, 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

if __name__ == '__main__':
    print('여기가 메인 함수')
    app.run() # app 시작! 사용자의 요청이 오는 것을 기다림

