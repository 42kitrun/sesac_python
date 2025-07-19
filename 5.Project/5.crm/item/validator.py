# 	입력값 유효성 검사 로직 분리

# backend/user/validator.py

def validate_create_user(data):
    errors = []

    # 이름 유무 체크
    if 'name' not in data or not data['name'].strip():
        errors.append('이름을 입력해주세요.')

    # 나이 숫자 여부 확인
    if 'age' in data and not isinstance(data['age'], int):
        errors.append('나이는 숫자여야 합니다.')

    return errors
