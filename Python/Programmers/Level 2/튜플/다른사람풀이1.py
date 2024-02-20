# 출처: 프로그래머스 다른 사람의 풀이
# Counter() 사용하여 코드가 더 짧아졌다.

def solution(s):

    s = Counter(re.findall('\d+', s))  # Counter(): iterable 객체를 넣으면 각 요소들의 빈도를 딕셔너리로 반환해준다
    # s.most_common() 추가해주면 빈도수가 높은 순으로 자동 정렬된다.
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
    # s.items(): 리스트 안에 딕셔너리의 key-value 쌍이 튜플 형태로 들어있다.
    # for문으로 순회하는 대신 map을 사용함

import re
from collections import Counter