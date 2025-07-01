import sys

sys.path.append("/Users/seSAC/src/sesac_python/4.Python/python_practice_problems/ch03")
import ridereader

rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''

rides_limit = {}
for line in rides.split('\n'):
    name, cmmin, cmmax = ridereader.read(line)
    rides_limit[name] = (cmmin, cmmax)
# print(rides_limit)

def allowedrides(height):
    assert type(height) == int
    '''**참(True)**이면 아무 일도 일어나지 않고,
    **거짓(False)**이면 AssertionError 예외를 발생'''

    result = []
    for name, (cmmin, cmmax) in rides_limit.items():
        # 둘 다 None
        if cmmin is None and cmmax is None:
            result.append(name)
        # 최소만
        elif cmmin is not None and cmmax is None:
            if height >= cmmin:
                result.append(name)
        # 최대만
        elif cmmin is None and cmmax is not None:
            if height <= cmmax:
                result.append(name)
        # 둘 다
        elif cmmin is not None and cmmax is not None:
            if cmmin <= height <= cmmax:
                result.append(name)
    return '\n'.join(result)


if __name__ == "__main__":
    while True:
        try:
            height = int(input("키를 입력하세요(숫자): "))
            break
        except ValueError:
            print("숫자를 입력해 주세요!")
    print(allowedrides(height))

