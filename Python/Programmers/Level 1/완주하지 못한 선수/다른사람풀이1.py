# 출처: 프로그래머스 다른 사람의 풀이
# Counter 객체끼리는 뺄셈이 가능하다.
    # 딕셔너리는 값을 뺄 수 없다. 카운터 객체라서 가능한 것
# 모든 참가자의 경우를 다 탐색해야 하기 때문에 for문 돌려서 탈락자 발견한 후 바로 미완주자 리턴 하는 것보다 시간은 더 걸린다고 함

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)  # Counter({'leo': 1})
    return list(answer.keys())[0]