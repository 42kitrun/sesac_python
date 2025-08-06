from flask import Flask, jsonify, request
import database as db

app = Flask(__name__, static_folder='public',static_url_path='')

db.create_table()

# 내 메모 리스트 담을곳 << 나는 sqlite3로 !
# todos = []

@app.route('/')
def home():
    return app.send_static_file('index.html')

# ------------------------------------------------------------

@app.route('/api/todo', methods=['GET'])
def get_todos():
    todos = [dict(todo) for todo in db.get_todos()]
    print(todos)
    return jsonify({'message':'성공적으로 저장됨',
                    'data' : todos})

@app.route('/api/todo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    print('todo to add:', todo)
    db.insert_user(todo)
    return jsonify({'message':'success',
                    'added_todo':todo})

@app.route('/api/todo', methods=['PATCH']) # 일부 수정
def update_todo():
    todo = request.get_json()
    print(todo)
    if todo.get('id') is not None:
        db.update_status(todo.get('id'), todo.get('status'))
        return jsonify({'message':'success',
                        'changed_todo': todo})
    
    return jsonify({'result':'fail'})

@app.route('/api/todo', methods=['DELETE'])
def delete_todo():
    todo_id = request.get_json()
    print(todo_id)
    if todo_id is not None:
        db.delete_todo(todo_id)
        return jsonify({'result':'success',
                        'deleted_id':todo_id})
    else:
        return jsonify({'result':'fail'})

# ------------------------------------------------------------

@app.route('/api/chat', methods=['GET'])
def get_chat():
    todos = [dict(todo) for todo in db.get_todos()]
    print(todos)
    return jsonify({'message':'성공적으로 저장됨',
                    'data' : todos})    

if __name__ == "__main__":
    app.run(debug=True)