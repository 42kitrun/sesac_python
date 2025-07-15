import sqlite3

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 미션 1-1. 여기 db로 부터 가져온 내용을 dict로 하고 싶으면??
    conn.row_factory = sqlite3.Row # 각각의 행이 tuple 이 아닌 dict로 반환된다
    return conn

# ---- 유저(user) -----
def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count
    
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_users_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

# ---- 상점(store) -----   
'''
def get_stores(search_text=None):
    conn = get_connection()
    cursor = conn.cursor()
    if search_text is None:
        cursor.execute(f"SELECT * FROM stores")
    else:
        cursor.execute(f"SELECT * FROM stores WHERE name = '{search_text}'")
    stores = cursor.fetchall()
    conn.close()

    # 1-2 미션. 미션1-1을 안했다면?? 여기에서 튜플형의 데이터를 dict형으로 변환해서~
    return [{'id':store[0], 'name':store[1], 'type':store[2], 'address':store[3]} for store in stores]
'''
def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()
    stores = [dict(r) for r in stores]
    return stores

def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()
    stores = [dict(r) for r in stores]
    return stores