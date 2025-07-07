from flask import Flask, jsonify
# from flask import jsonify

app = Flask(__name__)

users = [
    {'name':'Alice','age':25,'mobile':'050-1234-5678'},
    {'name':'Bob','age':30,'mobile':'050-2222-5678'},
    {'name':'Charlie','age':35,'mobile':'050-1234-5678'}
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    # 이름이 일치하는지
    # if 구문을 통해서, 입력받은 name이 실제로 위에 users에서 존재하는지 찾아서 user에 
    print("이름", name)

    user = None
    for u in users:
        if u['name'].lower() == name.lower():
          user = u
          break  # 반복문을 중단
    
    if user:
        return jsonify(user)
    else:
        return jsonify({'error':'User not found'}), 404
    
    # 만약 name에 숫자가 왔을때는, 나이로 검색을 하려면???

@app.route('/user/<int:age>')
def get_user_by_age(age):
    print("나이", age)
    
    user = None
    for u in users:
        if age == u['age']:
            user = u
            break  # 반복문을 중단
        
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=7700, debug=True)

