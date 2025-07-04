import uuid

class IdGenerator:
    def generate(self):
        return  uuid.uuid4()# uuid는 16바이트로 고정! if 문자열로 변환하면 일반적으로 32~36바이트(하이픈 포함)
