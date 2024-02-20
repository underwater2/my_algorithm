# Greedy 문제
# deque 사용해서 풀었다.
# 무게를 오름차순 정렬 후, 가장 작은 무게를 고정하고 가장 큰 무게들을 비교해간다.

from collections import deque

def solution(people, limit):
    people.sort()
    que = deque(people)
    answer = 0
    while que:
        now = que.popleft()
        while que and que[-1] > limit-now:
            que.pop()
            answer += 1
        if que:
            que.pop()
        answer += 1
    return answer