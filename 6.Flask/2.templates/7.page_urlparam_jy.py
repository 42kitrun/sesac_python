from flask import Flask, render_template
from math import ceil

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{i:04d}'} for i in range (1, 101)
]

# http://localhost:5000/pages/1
@app.route('/')
def index():
    page = 'all'
    previous_page=None
    next_page=None
    return render_template('users.html', users=users, page=page,previous_page = previous_page, next_page=next_page)

@app.route('/pages/<int:page>')
def users_pages(page):
    max_page = ceil(len(users)/10) # 한 페이지에 10개 목록
    page_num = lambda: page if  page <= max_page else None
    # filtered_users = [user for user in users if ceil(user['id']/10) == int(page)] # 매번 전체 id를 계산해야하니 성능이 안좋음
    # start_user, end_user를 계산해서 slicing 하는 방향으로 다시
    filtered_users = users[(page-1)*10 : page*10]
    previous_page= lambda: page -1 if 0 < page-1 < max_page else None
    next_page=lambda: page +1 if  page+1 <= max_page else None
    return render_template('users.html', users=filtered_users, page=page_num(), prev_page = previous_page(), next_page=next_page())

if __name__ == "__main__":
    app.run(debug=True, port = 7800)