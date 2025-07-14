from flask import Flask, jsonify, request
from flask_cors import CORS
# pip install flask-cors

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

todoList=[
    {"todo":"일찍 일어나기", "status":0},
    {"todo":"매일 운동하기", "status":1}
]

@app.route('/api/todo')
def todo():
    return jsonify(todoList) 

@app.route('/api/upload', methods=['POST'])
def upload():
    getTodoList = request.get_json()
    print(getTodoList)
    if request.method == 'POST' and getTodoList['todo']:

        todoList.append(
            {
                'todo':getTodoList['todo'],
                "status":getTodoList['status']
            }
        )
        return jsonify({'result':'success'})

    return jsonify({'result':'fail'})

@app.route('/api/update', methods=['PATCH'])# 일부 수정
def update():
    getTodoList = request.get_json()
    print(getTodoList)
    if request.method == 'PATCH' and getTodoList['todo'] is not None:
        global todoList # 함수 안에서 전역 변수에 새 값을 할당하려면 global이 필요하다! 안 쓰면 함수 안에서만 동작하고, 밖에 images에 영향이 없다.
        for todo in todoList:
            if todo['todo'] == getTodoList['todo']:
                todo['status'] = getTodoList['status']
                return jsonify({'result':'success'})
    
    return jsonify({'result':'fail'})

@app.route('/api/delete', methods=['DELETE'])
def delete():
    getTodoList = request.get_json()
    if request.method in ['DELETE'] and getTodoList['todo'] is not None:

        global todoList # 함수 안에서 전역 변수에 새 값을 할당하려면 global이 필요하다! 안 쓰면 함수 안에서만 동작하고, 밖에 images에 영향이 없다.
        todoList = [todo for todo in todoList if todo['todo'] != getTodoList['todo']]
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'fail'},404)

if __name__ == "__main__":
    app.run(debug=True, port=7890)
    