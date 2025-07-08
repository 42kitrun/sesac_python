from flask import Flask, render_template

app = Flask(__name__, static_folder="my_static")

# static 폴더는 바꿀수는 있지만 굳이 바꿀 필요는 없음
# static 이라고 폴더명을 정해주며, 그곳은 자동으로 외부에 노출된다.(img, html, )
# 3. 그래서 index 안에서 static을 전달할때는 하드코딩해도 동작은 하지만

@app.route('/')
def index():
    return render_template('index.html')
# 이미지 등 정적 파일을 브라우저가 서버에게 요청함



if __name__ == '__main__':
    app.run(debug=True, port=7890)