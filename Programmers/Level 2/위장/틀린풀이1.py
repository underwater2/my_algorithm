# 어떤 종류의 옷을 입는지 조합으로 구하여 풀었다.
    # tc1 시간초과

from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    dt = defaultdict(list)
    for c in clothes:
        dt[c[1]].append(c[0])
    for i in range(1, len(dt)+1):  # 입을 옷 종류 개수
        for comb in combinations(dt, i):  # 옷 종류의 조합 구하기
            cnt = 1
            for c in comb:
                cnt *= len(dt[c])
            answer += cnt
    return answer