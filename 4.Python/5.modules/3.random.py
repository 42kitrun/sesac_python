# https://docs.python.org/ko/3.13/library/random.html
# 무작위 숫자 만들기
import random #as rand

print('랜덤 숫자: ', random.randint(1,100)) # 1부터 100까지의 양수를 다 포함하는 랜덤 숫자를 생성

# 주사위 던지기 구현
def roll_dice():
    # number = random.randint(1,6)
    # return number
    return random.randint(1,6)

print(f'주사위 던진 결과: {roll_dice()}')

# 이 주사위를 100번 던져보고, 1000도 해보고, 10000번도 던져서... 각 숫자가 나올 확율을 출력해보시오
def dice(num):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0

    for i in range(num):
        result = roll_dice()
        if result == 1:
            num1 += 1
        elif result ==2 :
            num2 +=1
        elif result ==3 :
            num3 +=1
        elif result ==4 :
            num4 +=1
        elif result ==5 :
            num5 +=1
        elif result ==6 :
            num6 +=1

    
    print(f'1이 나온 횟수 : {num1}, 확률 : {num1/num:.2%}')
    print(f'2이 나온 횟수 : {num2}, 확률 : {num2/num:.2%}')
    print(f'3이 나온 횟수 : {num3}, 확률 : {num3/num:.2%}')
    print(f'4이 나온 횟수 : {num4}, 확률 : {num4/num:.2%}')
    print(f'5이 나온 횟수 : {num5}, 확률 : {num5/num:.2%}')
    print(f'6이 나온 횟수 : {num6}, 확률 : {num6/num:.2%}')


def dice2(num):
    count = [0,0,0,0,0,0]
    
    for i in range(num):
        result = roll_dice()
        if result == 1:
            count[result-1] += 1
        elif result ==2 :
            count[result-1] +=1
        elif result ==3 :
            count[result-1] +=1
        elif result ==4 :
            count[result-1] +=1
        elif result ==5 :
             count[result-1] +=1
        elif result ==6 :
            count[result-1] +=1

    
    print(f'1이 나온 횟수 : {count[0]}, 확률 : {count[0]/num:.2%}')
    print(f'2이 나온 횟수 : {count[1]}, 확률 : {count[1]/num:.2%}')
    print(f'3이 나온 횟수 : {count[2]}, 확률 : {count[2]/num:.2%}')
    print(f'4이 나온 횟수 : {count[3]}, 확률 : {count[3]/num:.2%}')
    print(f'5이 나온 횟수 : {count[4]}, 확률 : {count[4]/num:.2%}')
    print(f'6이 나온 횟수 : {count[5]}, 확률 : {count[5]/num:.2%}')

# for문으로 반복해서 결과를 취합해서, 위 내용을 출력하시오
def roll_dices(numbers):
    counts = [0,0,0,0,0,0]

    for i in range(numbers):
        result = roll_dice()
        # 짧은게 좋은건데 일주일 후에 봐서 이해가 안돼면? 복잡한 코드가 된것...
        counts[result -1] += 1 

    # 하나하나 개별 숫자를 6번 비교해서
    # if result == 1:
    #         count[result-1] += 1
    #     elif result ==2 :
    #         count[result-1] +=1
    #     elif result ==3 :
    #         count[result-1] +=1
    #     elif result ==4 :
    #         count[result-1] +=1
    #     elif result ==5 :
    #          count[result-1] +=1
    #     elif result ==6 :
    #         count[result-1] +=1

    for i, n in enumerate(counts):
        print(f'{i+1}이 나온 횟수 : {n}, 확률 : {n/numbers:.2%}')
        
# roll_dices(100_000)

# 딕셔너리라는 자료구조이고, key:value 라는 형태로 정의해서 
def roll_dices2(numbers):
    # 하드코딩 지양
    # 여기서의 키는 주사위 숫자 자신을 바로 의미함
    # counts2 = {1:0,2:0,3:0,4:0,5:0,6:0}
    counts2 = {i:0 for i in range(1,7)}

    for i in range(numbers):
        result = roll_dice()
        counts2[result] += 1 

    for k, v in counts2.items():
        print(f'{k}이 나온 횟수 : {v}, 확률 : {v/numbers:.2%}')

roll_dices2(100_000)