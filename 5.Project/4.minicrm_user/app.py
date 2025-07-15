import database as db
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    if request.args is None:
        users = db.get_users()
        return render_template('index.html', users=users)

    page = request.args.get('page', default=1, type=int) # 받은거를 Int로 변환시켜주겠다
    items_per_page = 10 # 10개, 20개, 30개..

    # 전체 유저수 가져오기
    user_count = db.get_user_count()
    total_page = user_count / items_per_page # 사용자 수가 나눠서 딱 떨어지지 않으면?? 사용자가 1004

    #users = db.get_users()
    users = db.get_users_per_page(page, items_per_page)
    return render_template('index.html', users=users, page=page)

if __name__ == '__main__':
    app.run(debug=True, port=7890)