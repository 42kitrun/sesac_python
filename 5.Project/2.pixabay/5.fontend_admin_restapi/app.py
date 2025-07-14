from flask import Flask, jsonify, request, abort
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
    
    return jsonify(results) 

@app.route('/api/upload', methods=['POST'])
def upload():
    print(request.files, request.form)
    image = request.files['image']
    filename = request.form['filename']
    keywords =  request.form['keywords']

    print(image, filename, keywords)
    
    if request.method == 'POST' and request.files is not None:

        if filename == '' or filename is None:
            return abort(404)

        images.append(
            {
                'filename':filename,
                "keywords":keywords.split(',')
            }
        )
        if allowed_file(filename):
            # 파일 저장하기 - 현재폴더의 uploads 안에 받은 파일명으로 저장하기
            filepath = os.path.join( 'static','img', filename)
            os.makedirs(os.path.join( 'static','img'), exist_ok=True)  # 폴더가 없으면 생성
            image.save(filepath)
            # filename : file.filename, keyword : 
            print( '파일 업로드에 성공하였습니다.')
            return jsonify({'result':'success'})
        else:
            print( '허용되지 않는 파일입니다.')
            jsonify({'result':'허용되지 않는 파일입니다.'})

    return jsonify({'result':'fail'})

@app.route('/api/update', methods=['PATCH'])# 일부 수정
def update():
    keywords = request.get_json()
    print(keywords)
    if request.method == 'PATCH' and keywords is not None:
        filename = keywords['filename']
        keyword = keywords['keywords'].split(',')
        global images # 함수 안에서 전역 변수에 새 값을 할당하려면 global이 필요하다! 안 쓰면 함수 안에서만 동작하고, 밖에 images에 영향이 없다.
        for file in images:
            if file['filename'] == filename:
                file['keywords'] = keyword
                return jsonify({'result':'success'})
    
    return jsonify({'result':'fail'})

@app.route('/api/delete', methods=['DELETE'])
def delete():
    if request.method in ['DELETE']:
        print(request.method)
        filename = request.get_json()
        print(filename)
        global images # 함수 안에서 전역 변수에 새 값을 할당하려면 global이 필요하다! 안 쓰면 함수 안에서만 동작하고, 밖에 images에 영향이 없다.
        images = [file for file in images if file['filename'] != filename]
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'fail'})

if __name__ == "__main__":
    app.run(debug=True, port=7890)
    