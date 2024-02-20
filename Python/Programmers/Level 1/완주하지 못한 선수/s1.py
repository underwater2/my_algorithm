# dict를 직접 만들지 않고 Counter 사용

from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    for p in part:
        try:
            if part[p] == comp[p]:
                continue
            else:  # comp의 value가 더 작음
                return p
        except:  # comp 내에 key가 없음
            return p
    answer = ''
    return answer