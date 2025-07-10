from flask import Flask, jsonify, url_for, request,redirect
from flask_cors import CORS
import os
# pip install flask-cors

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

images = [
    {"filename":"cat.jpeg", "keywords": ["cat", "pet", "cute"]},
    {"filename":"cat2.jpeg", "keywords": ["cat", "kitty", "cute"]},
    {"filename":"cat3.jpeg", "keywords": ["dog", "pet", "park"]},
    {"filename":"starbucks.png", "keywords": ["coffee", "logo", "starbucks"]}
]

ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif'}
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/api/admin')
def admin():
    results = []
    
    for item in images:
        item['img'] = os.path.join('img',item['filename'])
        results.append(item)
    
    return jsonify(results)  # 순수 BE개발자는 여기까지...

@app.route('/api/upload', methods=['GET','POST'])
def upload():
    if request.files:
        print(request.form) 
        file = request.files['file']

        if file.filename == '' or file.filename is None:
            return '파일이 올바르게 전송되지 않았습니다.'

        images.append(
            {
                'filename':file.filename,
                "keywords":request.form['keywords'].split(',')
            }
        )
        if allowed_file(file.filename):
            # 파일 저장하기 - 현재폴더의 uploads 안에 받은 파일명으로 저장하기
            filepath = os.path.join( 'static','img', file.filename)
            file.save(filepath)
            # filename : file.filename, keyword : 
            print( '파일 업로드에 성공하였습니다.')
        else:
            print( '허용되지 않는 파일입니다.')

    return redirect(url_for('admin'))

@app.route('/api/update/<filename>', methods=['GET,''POST'])
def update(filename):
    keywords = request.form.get('keywords')
    if request.method == 'POST' and keywords is not None:
        for file in images: 
            if file['filename'] == filename:
                file['keywords'] = keywords.split(',')
    
    return redirect(url_for('admin'))

@app.route('/delete/<filename>', methods=['GET','DELETE'])
def delete(filename):
    global images # 함수 안에서 전역 변수에 새 값을 할당하려면 global이 필요하다! 안 쓰면 함수 안에서만 동작하고, 밖에 images에 영향이 없다.
    images = [file for file in images if file['filename'] != filename]
    return jsonify({'result': 'ok'})

if __name__ == "__main__":
    app.run(debug=True, port=7890)
    