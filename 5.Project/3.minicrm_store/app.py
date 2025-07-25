from flask import Flask, render_template, request
import database as db

app = Flask('__name__')

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int) # 받은거를 Int로 변환시켜주겠다
    items_per_page = 10 # 10개, 20개, 30개..


    #users = db.get_users()
    users = db.get_users_per_page(page, items_per_page)
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port=7890)