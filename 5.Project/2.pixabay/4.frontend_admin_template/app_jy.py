from flask import Flask, jsonify, url_for, render_template, request,redirect
import os

app = Flask(__name__)

# UPLOAD_FOLDER = '5.Project/2.pixabay/4.frontend_admin_template/static/img'
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif'}
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

images = [
    {"filename":"cat.jpeg", "keywords": ["cat", "pet", "cute"]},
    {"filename":"cat2.jpeg", "keywords": ["cat", "kitty", "cute"]},
    {"filename":"cat3.jpeg", "keywords": ["dog", "pet", "park"]},
    {"filename":"starbucks.png", "keywords": ["coffee", "logo", "starbucks"]}
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/admin', methods=['GET','POST'])
def admin():
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

    results = [
    {
        "filename": item["filename"],
        "keywords": ', '.join(item["keywords"]),
        "img": url_for('static', filename=f'img/{item["filename"]}')
    }
    for item in images
    ]

    return render_template("admin.html", results=results)
    
@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join('./','static','img', filename)
    print(filepath,os.path.exists(filepath))
    if os.path.exists(filepath):
        os.remove(filepath)
        images.remove([file for file in images if filename in filepath and file.get('filename') == filename][0])
        # return '파일 삭제가 완료되었습니다.'
        return redirect(url_for('admin'))
    else:
        return '해당 파일은 존재하지 않습니다.'

if __name__ == "__main__":
    app.run(debug=True, port=7890)
    