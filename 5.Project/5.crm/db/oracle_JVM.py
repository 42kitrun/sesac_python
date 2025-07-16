import jpype
import jaydebeapi
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

'''

app.py (Flask 시작 시 start_jvm 호출 끝나면 stop_jvm 호출)
route.py (각 요청마다 connect_db만 호출)
'''
# db에 접속하는 함수를 작성하시오.
def start_jvm():
    if not jpype.isJVMStarted():
        jpype.startJVM(
            jpype.getDefaultJVMPath(),
            f"-Djava.class.path={os.getenv('ORACLE_JAR_PATH')}"
        )

def stop_jvm():
    if jpype.isJVMStarted():
        jpype.shutdownJVM()

def connect_db():
    user = os.getenv("ORACLE_USER")
    pw = os.getenv("ORACLE_PASSWORD")
    url = f"jdbc:oracle:thin:@{os.getenv('ORACLE_SERVICE_NAME')}?TNS_ADMIN={os.getenv('ORACLE_WALLET_PATH')}"
    jar = os.getenv("ORACLE_JAR_PATH")
    return jaydebeapi.connect("oracle.jdbc.driver.OracleDriver", url, [user, pw], jar)

# 테이블 생성함수 작성하시오.
def create_table():
    conn =  connect_db()
    cur = conn.cursor()
    
    cur.execute('''
        select 1+2 from dual
    ''')
    
    conn.commit()
    conn.close()
