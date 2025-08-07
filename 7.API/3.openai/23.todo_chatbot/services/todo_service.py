# service는 비즈니스 로직!
# 내 메모 리스트 담을곳

import database as db

db.create_table()
# 아래 변수들은 내부변수임.. 남들이 가져다 쓰지 마시오. private in java
# _todos = []
# _next_id = 1

def get_all():
    return db.get_todos() # [{'id': 1, 'todo': '숙제하기', 'status': 0}, {'id': 2, 'todo': '밥먹기', 'status': 0}]
    # return _todos

def get_all_to_string():# [{'id': 1, 'todo': '숙제하기', 'status': 0}, {'id': 2, 'todo': '밥먹기', 'status': 0}]
    # return [{'ID':t['id'],'할일':t['task'], "완료":t['done']} for t in _todos]
    return "\n".join([
        f"{t['id']}. {t['todo']} [{'완료' if t['status'] else '미완료'}]"
        for t in db.get_todos()
    ])
    # return "\n".join([
    #     f"{t['id']}. {t['task']} [{'완료' if t['done'] else '미완료'}]"
    #     for t in _todos
    # ])

def add(task):
    db.insert_todo(task)
    # global _next_id
    
    # new_todo = {'id': _next_id, 'task': task, 'done': False}
    # _todos.append(new_todo)
    # _next_id += 1
    # return new_todo

def toggle(todo_id):
    db.update_status(todo_id, status)
    # for todo in _todos:
    #     if todo['id'] == todo_id:
    #         todo['done'] = not todo['done']
    #         return todo  # 뭘 반납할지는 내가 정하면 됨

    # return None
      

def delete(todo_id):
    return db.delete_todo(todo_id) #
    # for todo in _todos:
    #     if todo['id'] == todo_id:
    #         _todos.remove(todo)
    #         return todo  # 지웠을때, 지운 아이템을 반환
    # return None

if __name__ == '__main__':
    # db.insert_todo('숙제하기')
    # db.insert_todo('밥먹기')
    # db.insert_todo('청소하기')
    print(db.get_todos())
    print(db.delete_todo(9))
    print(db.get_todos())