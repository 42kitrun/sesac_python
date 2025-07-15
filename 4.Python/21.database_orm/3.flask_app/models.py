from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # 객체를 print로 출력할때의 포맷 정의하는 함수
    def __repr__(self):
        return f'리스트나 튜플, 딕트 안에 있을때 [User {self.id}: {self.name}, {self.age}]'

    def __str__(self):
        return f'문자열 변환 [User {self.id}: {self.name}, {self.age}]'
