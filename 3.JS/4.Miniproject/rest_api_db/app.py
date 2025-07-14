from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import database as db

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

db.create_table()

@app.route('/api/todo')
def todo():
    todoList = [dict(todo) for todo in db.get_todos()]
    print(todoList)
    return jsonify(todoList) 

@app.route('/api/upload', methods=['POST'])
def upload():
    getTodoList = dict(request.get_json())
    print(getTodoList)
    if request.method == 'POST' and getTodoList['todo']:
        print(getTodoList['todo'])
        db.insert_user(getTodoList['todo'])
        return jsonify({'result':'success'})

    return jsonify({'result':'fail'})

@app.route('/api/update', methods=['PATCH'])# 일부 수정
def update():
    getTodoList = dict(request.get_json())
    print(getTodoList)
    if request.method == 'PATCH' and getTodoList['todo'] is not None:
        db.update_status(getTodoList['todo'], getTodoList['status'])
        return jsonify({'result':'success'})
    
    return jsonify({'result':'fail'})

@app.route('/api/delete', methods=['DELETE'])
def delete():
    getTodoList = dict(request.get_json())
    print(getTodoList)
    if request.method in ['DELETE'] and getTodoList['todo'] is not None:
        db.delete_todo(getTodoList['todo'])
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'fail'})

if __name__ == "__main__":
    app.run(debug=True, port=7890)
    