import sqlite3

MY_DATABASE = 'todo.db'

# db에 접속하는 함수를 작성하시오.
def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row # 각각의 행이 tuple 이 아닌 dict로 반환된다
    return conn

# 테이블 생성함수 작성하시오.
def create_table():
    conn =  connect_db()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            todo TEXT NOT NULL, 
            status INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    
# 데이터 삽입 함수
def insert_user(todo):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO todos (todo, status) VALUES (?, ?)", (todo, 0))
    
    conn.commit()
    conn.close()
    
# 데이터 조회 함수
def get_todos():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM todos')
    rows = cur.fetchall()  # 모든거 다
    
    conn.commit()
    conn.close()
    
    return rows  # 가져온 todo 반환

# 데이터 수정 함수
def update_status(todo, status):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('UPDATE todos SET status=? WHERE todo=?', (status, todo))
    
    conn.commit()
    conn.close()

# todo 삭제
def delete_todo(todo):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM todos WHERE todo=?', (todo,))
    
    conn.commit()
    conn.close()