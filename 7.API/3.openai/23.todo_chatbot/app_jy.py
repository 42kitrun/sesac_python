from flask import Flask, jsonify, request
import database as db

from langchain_core.prompts import ChatPromptTemplate   # 지금부터 할거 <- QA(Chat 모델)
from langchain_openai import ChatOpenAI # <- QA(Chat 모델)
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda 나중에 후처리가 필요할지도 모르니까

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='public',static_url_path='')

db.create_table()

# 1. 프롬프트 생성
prompt = ChatPromptTemplate.from_messages([
    ('system', 'You handle My todo List'),
    ('human', '나의 요청사항을 빠르고 정확하게 처리해줘. 나의 요청사항 : {user_input}'),
])

# 2. 모델 생성
llm = ChatOpenAI(model="gpt-3.5-turbo") # gpt-3.5-turbo <- chat 모델

# 3. 파서 생성
parser = StrOutputParser()

# 4. 체인 만들기 = LCEL (LangChain Expression Language)
chain = prompt | llm | parser

# 내 메모 리스트 담을곳 << 나는 sqlite3로 !
# todos = []

@app.route('/')
def home():
    return app.send_static_file('index.html')

# ------------------------------------------------------------

@app.route('/api/todo', methods=['GET'])
def get_todos():
    todos = db.get_todos()
    print(todos)
    return jsonify({'message':'성공적으로 저장됨',
                    'data' : todos})

@app.route('/api/todo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    print('todo to add:', todo)
    db.insert_todo(todo)
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

@app.route('/api/chat', methods=['POST'])
def get_chat():
    user_input = request.get_json().get('userInput')
    print(user_input)

    result = chain.invoke({'user_input':user_input})

    print("최종결과:", result)
    return jsonify({'message':'성공적으로 저장됨',
                    'ans' : result})    

if __name__ == "__main__":
    app.run(debug=True)