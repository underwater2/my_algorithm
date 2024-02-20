# 다른 코드
# https://ooyoung.tistory.com/74
# 파이썬 문자열 replace 함수 사용
    # 검색을 해보니 크로아티아 알파벳이 입력값에 있다면 그냥 한글자 알파벳으로 바꿔주는 방법이 있었다.
    # 치환을 끝낸 후 길이를 리턴하는 방법으로 구현해보았다.
    # 구현할때 dz= 가 z= 보다 앞에 있지 않으면 z=를 우선으로 바꿔버리게되므로 dz=가 z= 보다 앞에 있어야 한다.

import sys
sys.stdin = open('input.txt')

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))