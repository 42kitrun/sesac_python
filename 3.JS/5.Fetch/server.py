from flask import Flask, send_file, jsonify
# from flask_cors import CORS
# 여기다가 cors라이브러리를 추가해서 해결하거나, 또는, 프런트엔드를 내가 서빙해주거나..

app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    # return 'Hi~' 1가지
    return send_file('4.fetch.html') # 프런트엔드 파일을 서버가 제공

@app.route('/data')
def data():
    return jsonify({'result':'success','message':'여기가 data','greeting':'안녕하세요'})
# 현업은 result 사용 하지만 모던한 스타일은 404,200 등을 사용

if __name__ == '__main__':
    app.run(debug=True, port=7890)