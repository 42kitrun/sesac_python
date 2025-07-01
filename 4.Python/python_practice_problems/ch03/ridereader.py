def read(text):
    txt_list = text.split(':')
    if 'cm' not in txt_list[1]:
        cmmin = None
        cmmax = None
    elif '~' in txt_list[1]:
        str_cmmin,str_cmmax = txt_list[1].strip().replace('cm','').split('~')
        cmmin, cmmax = int(str_cmmin), int(str_cmmax)
    else:
        cmmin = int(txt_list[1].strip().split('cm')[0])
        cmmax = None

    return txt_list[0], cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

