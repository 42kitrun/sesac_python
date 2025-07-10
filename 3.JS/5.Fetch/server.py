from flask import Flask, send_file, jsonify
# from flask_cors import CORS
# 여기다가 corsfkdlqmfjflfmf cnrkgotj gorufgkrjsk, Ehsms, vmfjsxmdpsemfmf sork 서빙해주거나


app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    # return 'Hi~' 1가지
    return send_file('4.fetch.html') # 프런트엔드 파일을 서버가 제공

@app.route('/data')
def data():
    # return '안녕하세요~' # 이 경우가 api...?
    return jsonify({'result':'success','message':'여기가 data','greeting':'안녕하세요'})
# 현업은 result 사용 하지만 모던한 스타일은 404,200 등을 사용

if __name__ == '__main__':
    app.run(debug=True, port=7890)