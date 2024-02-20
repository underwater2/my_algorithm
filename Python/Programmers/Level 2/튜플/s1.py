# s 안에 많이 들어있는 숫자일수록 튜플의 앞자리를 차지한다.

import re

def solution(s):
    p = re.compile('[{},]+')
    nums = p.split(s)[1:-1]  # 리스트에 등장 숫자 모두 넣기
    hashli = dict()
    for num in nums:  # dict에 숫자 종류, 등장 횟수 저장
        if num in hashli:
            hashli[num] += 1
        else:
            hashli[num] = 1
    sortli = sorted(hashli.items(), key=lambda x: -x[1])  # 딕셔너리의 value로 내림차순 정렬
    answer = []
    for tup in sortli:
        answer.append(int(tup[0]))
    return answer