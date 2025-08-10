import os
import json
from dotenv import load_dotenv
from collections import deque

from openai import OpenAI

from services import todo_service as todo
import database as db

db.create_table()

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("API키가 없습니다!!")

client = OpenAI(api_key=API_KEY)

HISTORY = deque(maxlen=10) # 최대 10개를 담을수 있는 자료구조

def store_history(role, content):
    HISTORY.append({'role':role, 'content': content})

def build_prompt_message(system_prompt):
    messages = [{"role":"system", "content":system_prompt}]
    messages.extend(HISTORY)
    return messages

def handle_chat(question):
    story_history("user", question) # 사용자의 대화 내용 저장

    action = ask_gpt(question) # 우리의 대화 내용을 담아서 넣을거다.
    final_reponse = do_action(action)

    store_history("assistant", final_response) # 챗봇의 응답 내용을 저장
    return final_response

def ask_gpt(question):
    my_todo_list = todo.get_all_to_string() # todo 목록을 모두 가져온다.
    
    system_prompt1 = f"""
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
사용자의 TODO 항목과 질문에 대해서 간결하게 답변해 주세요.

[할 일 목록]
{my_todo_list}
"""  

    system_prompt2 = f"""
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
사용자의 TODO 항목과 질문에 대해서 최대한 이모티콘을 많이 사용해서 포악한 동물처럼 어흥~ 또는 멍멍~  형태로 답변해 주세요. 

[할 일 목록]
{my_todo_list}
"""  

    system_prompt3 = f'''
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
당신은 사용자의 질문에 대해서 아래 중에 하나를 골라서 action 을 선택하고 답변해야 합니다.
사용자의 TODO 항목과 질문에 대해서 JSON 포멧으로 최대한 간결하게 답변해 주세요.

[출력 형식]
{{ "action": "add", "item": [항목] }} - 할일을 추가해야 할 때
{{ "action": "delete", "item": [항목ID] }} - 할일을 안할꺼거나, 잘못 추가했을때
{{ "action": "update", "item": [항목ID] }} - 할일을 다했거나, 다한일을 다시 해야 할 때
{{ "action": "list" }} - 할일을 보여줘야 할 때
{{ "action": "nothing }} - 어떻게 판단해야할지 모를때 또는 TODO 리스트와는 쓸대없는 질문이 들어왔을때

[할 일 목록]
{my_todo_list}
'''

    system_prompt = system_prompt2
    print("내가 GPT에게 할 질문:\n", system_prompt)
    
    system_prompt = system_prompt3
    print("내가 GPT에게 할 질문:\n", system_prompt)
    
    user_history_messages = build_prompt_message(system_prompt3)
    print("내가 GPT에게 최종적으로 던질 모든 메세지:\n", user_history_messages)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=user_history_messages
    )
    
    reply = response.choices[0].message.content.strip() # { "action": "add", "item": [항목] }
    print("GPT의 RAW응답값:", reply) # 어떠한 형태의 답변들이 나올지 살펴보고, 추후 예외처리에 고려한다.
    
    # try catch로 감싼다.
    my_action = json.loads(reply) # { "action": "add", "item": [항목] }
    print("내가 실행할 ACTION:\n", my_action)

    return my_action

def do_action(my_action):
    action = my_action.get('action')
    text = my_action.get('item')
    
    print(f"처리할 준비: {action}, {text}")
    if action == 'add':
        print("추가할 코드 짜기:", my_action)
        todo.add(text)
        return f'할 일 "{text}" 를 추가하였습니다.'
    
    if action == 'delete':
        print("삭제할 코드 짜기:", my_action)
        todo.delete(int(text))
        return f'할 일 "{text} 를 삭제하였습니다.'
    
    if action == 'list':
        print("보여줄 코드 짜기:", my_action)
        my_todos = todo.get_all_to_string()
        return  f"다음 할일들이 있습니다.\n{my_todos}"
    
    if action == 'update':
        print("수정할 코드 짜기:", my_action)
        todo.toggle(int(text))
        return f'다음 항목 "{text}" 을 수정했습니다.'
    
    return f"잘 이해하지 못했습니다. 다시 한번 말씀해 주세요."

# ------------ 수업시간 실습 --------------------------

def jy_do_action(my_action):
    action = my_action.get('action')
    text = my_action.get('item')

    print(f"처리할 준비: {action}, {text}")
    if action == 'add': 
        item = my_action.get('item')        
        todo.add(item)
        reply = f"{item}을 todo에 추가했습니다."
    elif action == 'delete':
        item = my_action.get('item') 
        # [{'id': 1, 'task': '휴지', 'done': False}]
        item_id = next((i['id'] for i in my_todo_list if i["task"] == item), None)
        todo.delete(item_id)
        reply = f"{item}을 todo에서 삭제했습니다."
    elif action == 'list':    
        list_ = todo.get_all()
        todo_list = [item.get('task') for item in list_]
        reply = f"전체 할일은 {todo_list}입니다."
    elif action == 'update':
        item = my_action.get('item') 
        # [{'id': 1, 'task': '휴지', 'done': False}]
        item_id = next((i['id'] for i in my_todo_list if i["task"] == item), None)
        todo.toggle(item_id)
        reply = f"{item}을 todo에서 상태변경 완료했습니다."
    else:
        print("아무것도 안하기")
        reply = "사용자에게 올바른 입력하라고 말하기"
    
    return reply
