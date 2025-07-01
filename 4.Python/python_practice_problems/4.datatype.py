## 4.2.1. 연습 문제: 아이돌 팬 (1)
newjeans = ['철수', '영희', '민수', '지현', '서연']
ive = ['영희', '민수', '지수', '서연', '하나']
espa = ['철수', '지현', '지수', '서연', '나영']
def idol_fan():
    intersect = [i for i in newjeans if i in ive]
    print([i for i in intersect if i not in espa])

## 4.2.3 연습 문제: 회문 판별 함수 만들기
# quiz 1,2,3
def palindrome(name:str):
    name = name.strip().lower()
    return name == name[::-1]

# print(palindrome('anna'))

## 4.2.4 연습 문제: 각 자리 숫자의 합을 구하는 함수(리스트를 이용)
# def sumOfDigits(num:int):
#     return sum([int(n) for n in list(str(num))])

# print(sumOfDigits(643))

## 4.2.5 연습 문제: 줄기와 잎 그림
stem_leaf = []
def make_stem_leaf(arr:list):
    stem_leaf.append(arr)
    return stem_leaf

make_stem_leaf([0, 0, 2, 4, 7, 7, 9])
make_stem_leaf([11, 11, 13, 18])
# print(make_stem_leaf([20]))

def print_stem_leaf():
    for i in range(len(stem_leaf)):
        print(f'{i}: {stem_leaf[i]}')
# print_stem_leaf()        

## 4.2.6 연습 문제: 각 자리 숫자의 합을 구하는 함수(map()을 이용)
def sumOfDigits(num:int):
    return sum(list(map(lambda x : int(x) ,list(str(num)))))
# print(sumOfDigits(47253))

## 4.2.7 연습 문제: 소수 구하기
def prime_number(num):
    num_list = list(range(2, num+1))  # 찾고자 하는 범위의 자연수를 나열
    prime_numbers = []

    while num_list:
        remove_num = num_list.pop(0)
        num_list = list(filter(lambda x: x % remove_num!=0, num_list))
        prime_numbers.append(remove_num)

    print(prime_numbers)
    return prime_numbers

# prime_number(23)

## 4.3.1 연습 문제: 두 수의 사칙연산 프로그램 만들기
def compute(num_string):
    a, b = num_string.split(' ')
    a = int(a)
    b = int(b)
    return f'{a+b}{a-b}{a*b}{a/b}'

## 4.3.2 연습 문제: 내일의 날짜 구하기(1)
import datetime
def tomorrow():
    input_string = input('날짜 (예. 2017 10 2):')
    yyyy, mm, dd = input_string.split(' ')

    today = datetime.datetime(int(yyyy),int(mm),int(dd))
    tomorrow = today + datetime.timedelta(days=1)
    print(f"{today.strftime('%m/%d/%Y')}\n{tomorrow.strftime('%m/%d/%Y')}")

# tomorrow()

## 4.3.3 연습 문제: 여러 수의 사칙연산 프로그램 만들기
def compute_int(a,b,c,d):
    return a+b,a-b,a*b,a/b

def compute_multiple(num_string):
    num_list = num_string.split(' ')
    f_num =int(num_list[0])
    s_num =int(num_list[1])

    result = {'plus':f_num+s_num
              ,'minus':f_num-s_num
              ,'gop':f_num*s_num
              ,'slash':f_num/s_num}
    for num in num_list[2:]:
        result['plus'] += int(num)
        result['minus'] -= int(num)
        result['gop'] *= int(num)
        result['slash'] /= int(num)
    # print(result)
    return f"{result['plus']} {result['minus']} {result['gop']} {result['slash']}"
# print(compute_multiple('16 4 2'))

## 4.4.1 연습 문제: 숫자 읽기(0~9)
def korean_number(num:int):
    return {1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구',0:'영'}[num]
# print(korean_number(3))

## 4.4.2 연습 문제: 한자 성어
def hanja():
    table = {
'江湖之樂(강호지락)':	'자연을 벗 삼아 누리는 즐거움'
,'欲速不達(욕속부달)':	'빨리 하고자 하면 이루지 못함'
,'積小成大(적소성대)':	'작은 것을 쌓아 큰 것을 이룸'
,'勤儉節約(근검절약)':	'부지런하고 알뜰하게 재물을 아낌'
,'經世濟民(경세제민)':	'세상을 다스리고 백성을 구제함'
,'塞翁之馬(새옹지마)':	'인생의 길흉화복은 변화가 많아서 예측하기가 어려움'
,'好事多魔(호사다마)':	'좋은 일에는 흔히 방해되는 일이 많음'
,'桑田碧海(상전벽해)':	'세상일의 변천이 심함'
,'自業自得(자업자득)':	'자기가 저지른 일의 결과를 자기가 받음'
,'因果應報(인과응보)':	'원인과 결과가 상응하여 보답한다'
,'愚公移山(우공이산)':	'어떤 일이든 끊임없이 노력하면 반드시 이루어짐'
}

    for line in table.keys():
        btn = input('Enter를 누르세요...')
        print(line)
        print(table[line])

# hanja()

## 4.5.1 연습 문제: 아이돌 팬 (2)
newjeans = {'철수', '영희', '민수', '지현', '서연'}
ive = {'영희', '민수', '지수', '서연', '하나'}
espa = {'철수', '지현', '지수', '서연', '나영'}

# print(newjeans.intersection(ive).difference(espa))

## 4.5.2 연습 문제: 주사위 눈의 합
def plus():
    dice1 = (1, 2, 3, 4, 5, 6)
    dice2 = (2, 3, 5, 7, 11, 13)
    result = set()
    for  n in dice1:
        for m in dice2:
            result.add(n+m)
    return result

# print(plus())

## 4.5.3 연습 문제: 끝말 잇기 (1)
history = set()
words = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']
doum = {'냑':'약','략':'약','냥':'양','량':'양','녀':'여','려':'여'
        ,'녁':'역','력':'역','년':'연','련':'연','녈':'열','렬':'열'
        ,'념':'염','렴':'염','녕':'영','령':'영','녜':'예','례':'예'
        ,'뇨':'요','료':'요','뉴':'유','류':'유','뉵':'육','륙':'육'
        ,'니':'이','리':'이','라':'나','락':'낙','란':'난','란':'난'
        ,'랄':'날','람':'남','랍':'납','랑':'낭','래':'내','랭':'냉'
        ,'렵':'엽','로':'노','록':'녹','론':'논','롱':'농','뢰':'뇌'
        ,'룡':'용','루':'누','륜':'윤','률':'율','륭':'융','륵':'늑'
        ,'름':'늠','릉':'능','린':'인','림':'임','립':'입'
        ,}

def words_game():
    print('<시작>끝말잇기를 하자. 내가 먼저 말할게.')
    word = '기차'
    while word:
        # computer
        print(word)
        if word in words:
            words.remove(word)
        history.add(word)
        #사람
        input_word = input(f'"{word[-1]}"로 끝나는 단어 : ')
        if input_word == '졌어':
            print('내가 이겼어!<끝>')
            return
        elif  doum[word[-1]] == input_word[0]:
            pass
        elif input_word in history:
            print('아까 했던 말이야. 내가 이겼어!<끝>')
            return
        elif not input_word.startswith(word[-1]):
            print(f'글자가 안 이어져. 내가 이겼어!<끝>')
            return
        elif len(input_word) < 2:
            print(f'한 글자는 안돼. 내가 이겼어!<끝>')
            return
        
        if input_word in words:
            words.remove(input_word)
        history.add(input_word)

        word = find_word(input_word)
        continue

def find_word(prev_word):
    try:
        next_word = list(filter(lambda x : x.startswith(prev_word[-1]),words))[0]
        if next_word not in history:
            return next_word
        else:
            print('모르겠다. 내가 졌어.<끝>')
            return ''   
    except:
        print('모르겠다. 내가 졌어.<끝>')
        return ''
    
words_game()