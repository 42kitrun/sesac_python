import oracledb
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Flask 초기에서 1번만 호출 (중복호출 안전)
oracledb.init_oracle_client(
    lib_dir=os.getenv("INSTANT_CLIENT_PATH"),
    config_dir=os.getenv("ORACLE_WALLET_PATH")
)

# row factory 대체
def dict_r(cursor):
    columns = [col[0].lower() for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
    

def connect_db():
    """ 오라클 연결 반환 """
    return oracledb.connect(
        user = os.getenv("ORACLE_USER"),
        password = os.getenv("ORACLE_PASSWORD"),
        dsn = os.getenv("ORACLE_SERVICE_NAME")
    )


def get_users( limit_rownum = 0, start_rownum = 0):
    sql = "SELECT * FROM users WHERE 1=1 "
    if start_rownum:
        sql += f'OFFSET {start_rownum} ROWS'
    if limit_rownum:
        sql += f'FETCH NEXT {limit_rownum} ROWS ONLY'

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(sql)

    stores = dict_r(cursor)
    
    conn.close()
    return stores

if __name__ == '__main__':
    print(get_stores())