from flask import Flask, render_template, request
from math import ceil

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{i:04d}'} for i in range (1, 101)
]

# http://localhost:5000/?pages=1
@app.route('/')
def index():
    pages = request.args.get('pages')
    max_page = ceil(len(users)/10)

    page = ''
    filtered_users =[]
    previous_page=None
    next_page=None

    if pages == '' or pages is None:
        page = 'all'
        filtered_users = users
        
    elif pages in '1023456789' and int(pages) <= max_page:
        page = int(pages)
        filtered_users = [user for user in users if ceil(user['id']/10) == page]
        if 0 < page-1 < max_page:
            previous_page = f'?pages={page -1}'
        else:
            previous_page = None
        if page+1 <= max_page:
            next_page = f'?pages={page +1}'
        else:
            next_page = None

    else:
        page = None
        filtered_users = None
    
    return render_template('users.html', users=filtered_users, page=page, prev_page = previous_page, next_page=next_page)

if __name__ == "__main__":
    app.run(debug=True, port = 7800)