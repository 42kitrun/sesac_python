import sqlite3

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 미션 1-1. 여기 db로 부터 가져온 내용을 dict로 하고 싶으면??
    conn.row_factory = sqlite3.Row # 각각의 행이 tuple 이 아닌 dict로 반환된다
    return conn
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

    # 미션1-2. 미션1-1을 안했다면?? 여기에서 튜플형의 데이터를 dict형으로 변환해서 반납하고 싶으면??
    # stores_dict = []
    # for s in stores:
    #     stores_dict.append({
    #         'id': s[0],
    #         'name': s[1],
    #         'type': s[2],
    #         'address': s[3]
    #     })
    # stores_dict = [{'id':s[0], 'name':s[1], 'type':s[2], 'address':s[3]} for s in stores]    
    
    # return [{'id':store[0], 'name':store[1], 'type':store[2], 'address':store[3]} for store in stores]
    return [dict(r) for r in stores]

def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM stores WHERE Name LIKE ?",(name,))
    # cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()

    # 1-2 미션. 미션1-1을 안했다면?? 여기에서 튜플형의 데이터를 dict형으로 변환해서~
    # return [dict(r) for r in stores]
    return [{'id':store[0], 'name':store[1], 'type':store[2], 'address':store[3]} for store in stores]