from abc import ABC, abstractmethod
from datetime import datetime
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

# 커넥션 풀 싱글톤 클래스 정의
class OracleDBPool:
    _pool = None

    @classmethod
    def init_pool(cls):
        if cls._pool is None:
            cls._pool = oracledb.create_pool(
                user=os.getenv("ORACLE_USER"),
                password=os.getenv("ORACLE_PASSWORD"),
                dsn=os.getenv("ORACLE_SERVICE_NAME"),
                min=2,
                #   최소 커넥션 개수
                # 이 풀은 시작할 때부터 최소 2개의 DB 연결을 열어둡니다.
                # 즉, 앱이 켜지면 바로 2개의 연결을 만든 상태로 대기합니다.
                # 이유: 바로 사용할 수 있게 미리 준비해놓기 위해
                # 실무에서는 min=1~5 정도로 설정
                max=5,
                #   최대 커넥션 개수 : 동시에 사용할 수 있는 커넥션 수의 최대 개수
                # 만약 10명의 사용자가 동시에 요청 → 각자 하나씩 커넥션을 사용
                # 11번째 요청은 대기하거나 에러 발생(선택옵션)
                # 서버 사양/트래픽에 따라 적절히 조절 필요
                increment=1,
                #    부족할 때 새로 추가할 커넥션 개수
                # 현재 풀에 여유가 없으면 1개씩 커넥션을 추가로 생성
                # 예:현재 커넥션이 다 사용 중인데 새 요청이 오면
                # 최대수(max) 제한까지 1개씩 점진적으로 커넥션을 늘림
                # increment=2~5 등으로 변경도 가능 (성능/속도 튜닝용)
            )
        return cls._pool

    @classmethod
    def get_connection(cls):
        if cls._pool is None:
            raise Exception("커넥션 풀이 초기화되지 않았습니다! 먼저 init_pool() 호출하세요.")
        return cls._pool.acquire()

    @classmethod
    def release_connection(cls, conn):
        if cls._pool:
            cls._pool.release(conn)

class OracleConnection:
    def __enter__(self):
        self.conn = OracleDBPool.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("예외 발생:", exc_type, exc_val)
        self.cursor.close()
        OracleDBPool.release_connection(self.conn)