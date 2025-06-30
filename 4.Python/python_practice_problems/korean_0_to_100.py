def korean_number(num):
    try:
        ch = int(num)
        if ch < 0 or ch >100 :
            raise ValueError('0 이상 100 이하의 정수만 입력해주세요!')
    except:
         print('0 이상 100 이하의 정수만 입력해주세요!')

    single_pron = ['십','일','이','삼','사','오','육','칠','팔','구']
    pron = []

    if num == 0 :
        return '영'
    elif num == 100:
        return '백'
    elif num < 10:
        return single_pron[num]
    else:
        for i in list(str(num)):
            pron += [single_pron[int(i)]]
        pron.insert(1,'십')
        return ''.join(pron)