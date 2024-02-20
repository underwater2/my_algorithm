# 입력값의 수를 알려주지 않은 문제였다.
    # https://joewithtech.tistory.com/26
    # 이 문제의 목적은 문자열을 올바르게 입력받고 파일의 끝(EOF)을 올바르게 판단하는 법을 연습하는 것입니다.
    # 총 몇 줄이 주어진다 등의 정보는 절대 입력으로 주지 않습니다.
    # 또한 단순히 키보드로 입력 내용만 적고 프로그램이 종료되지 않은 상태까지만 봐서는 EOF를 제대로 처리했는지 알 수 없습니다.
    # 더 이상 읽을 게 없을 때 프로그램을 종료하는 법을 알아야 합니다.
    # 파이썬의 경우
        #(Python) input()은 EOFError를 발생시킵니다.
        #(Python) sys.stdin.readline()은 빈 문자열을 반환합니다.
# 문자열의 공백은 strip(), lstrip(), rstrip() 메서드로 제거한다.
# 딕셔너리를 key, value 각각으로 정렬하기
    # https://kkamikoon.tistory.com/138
# input = sys.stdin.readline 에서 NameError 발생
    # import sys 를 빼고 제출했기 때문에 난 거였다.

import sys
sys.stdin = open('input.txt')

species = 0
n = 0
di = dict()

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    try:
        di[tree] += 1
    except:
        di[tree] = 1
        species += 1
    n += 1
sdi = sorted(di.items())
for i in sdi:
    # print(i[0] + ' ' + str(round(i[1]/n * 100, 4)))
    # 위처럼 하면 틀린다.
        # python round 함수 작동방식이 좀 독특해서 그럽니다
        # https://docs.python.org/ko/3/library/functions.html?highlight=round#round
        # 예를 들어, round(0.5) 와 round(-0.5) 는 모두 0 이고, round(1.5) 는 2 입니다
    print("%s %.4f" % (i[0], i[1]/n * 100))
        # 소수점 4자리까지 반올림하여 출력해줌
