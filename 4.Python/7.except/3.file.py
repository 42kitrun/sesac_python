# https://docs.python.org/ko/3.13/tutorial/errors.html
try:
    with open('hello.txt','r') as file:
        contents = file.read()

    print('파일내용 :', contents)
except FileExistsError:
    print('파일이 존재하지 않습니다')
except IOError:
    print('파일을 읽을 수 없습니다')
except:
    print('알 수 없는 오류입니다')