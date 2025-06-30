# https://docs.python.org/ko/3.13/library/os.html#module-os
import os

# 현재 디렉토리를 가져온다 cwd = current working directory
print('현재 작업 디렉토리는: ', os.get_cwd())

new_directory = 'sesac1234'
# path 조심하세요 악성코드가 될수도 있어요
os.mkdir(new_directory) # python이 시스템에 요청 : 시스템콜
print('생성완료')

os.chdir(new_directory)
print('이동완료')

os.chdir('..') # .은 현재 디렉토리, .. 부모 디렉토리
print('부모 디렉토리로 이동완료')

os.rmdir(new_directory)
print('삭제완료')