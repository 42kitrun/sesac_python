from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # 이때 이 파일은 무조건 templates 라는 폴더 안에 있어야 함.

if __name__ == '__main__':
    # app.run(debug=True, port =7800)
    app.run(debug=True, host="0.0.0.0", port =7800)
    '''
    host = "0.0.0.0"   : 같은 네트워크에 있는 다른 컴퓨터(예: 스마트폰, 노트북)에서도 내 컴퓨터의 IP 주소로 접속 가능
    host = "127.0.0.1" : 내 컴퓨터에서만 접속 허용
    '''