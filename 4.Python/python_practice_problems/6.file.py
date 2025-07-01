## 6.2.1 밴드이름 짓기 (2)
import random

color = []
food = []

with open('4.Python/python_practice_problems/color.txt','r') as f_color:
    color = list(map(lambda x : x.strip(),f_color.readlines()))

with open('4.Python/python_practice_problems/food.txt','r') as f_food:    
    food = list(map(lambda x : x.strip(),f_food.readlines()))

color_num = random.randint(0,len(color))
food_num = random.randint(0,len(food))

# print(color[color_num], food[food_num])

## 6.2.2 연습 문제: 비밀 메시지
content = ''
with open('4.Python/python_practice_problems/postcard.txt','r') as f:
    for line in f.readlines():
        if line[0] == ' ' or line.split(' ')[0] == 'Dear':
            pass
        else:
            trans_table = line.maketrans( {'.':'',',':'',':':''})
            content += ' '.join(line.translate(trans_table).upper().split()[:2])+ ' '

# print(content)

## 6.2.2. 연습 문제: 끝말 잇기 (3)
# 글자가 안 이어져. 내가 이겼다!<끝>
# 모르겠다. 내가 졌어.<끝>
# 아까 했던 말이야. 내가 이겼어!<끝>
history = set()
words = []
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

with open('4.Python/python_practice_problems/korean_words.txt','r') as f:
    words = list(map(lambda x : x.strip(),f.readlines()))

def words_game():
    print('<시작>끝말잇기를 하자. 내가 먼저 말할게.')
    word = '기차'
    while word:
        # computer
        print(word)
        if word in words:
            words.remove(word)
        history.add(word)
        # print('history',history)
        # print('len(words) :',len(words))
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
    
# words_game()

## 6.2.3 연습 문제: 영어 퀴즈
sentence = []
with open('4.Python/python_practice_problems/ko_en.txt','r', encoding='cp949') as f:
    sentence = list(map(lambda x : x.strip(),f.readlines()))
dict_sentence = {s.split('\t')[0]:s.split('\t')[1] for s in sentence if 'ko' not in s}

def en_quiz():
    for  s in set(dict_sentence.keys()):
        response = input(f'Write the following sentence in English.\n{s}\n\nyour answer: ')
        if dict_sentence[s] == response :
            print('\nresult: Correct!\n')
            print('-'*50)
            continue
        else:
            print('\nresult: Not Correct!')
            print(f'right answer: {dict_sentence[s]}')
            return
        
# en_quiz()

## 6.3.1 연습 문제: 애국가
with open('4.Python/python_practice_problems/out.txt','w',) as f:
    for num in range(1,5):
        with open(f'4.Python/python_practice_problems/korean_national_anthem_{num}.txt','r', encoding='cp949') as song:
            f.write(f'korean_national_anthem_{num}.txt\n')
            f.write('-'*28+'\n')
            f.write(song.read()+'\n\n')



