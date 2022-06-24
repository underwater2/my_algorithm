# 우선순위 큐 개념 이해
    # https://suyeon96.tistory.com/31
# 파이썬의 우선순위 큐(PriorityQueue) 사용법
    # https://www.daleseo.com/python-priority-queue/
    # from queue import PriorityQueue
# [파이썬] heapq 모듈 사용법
    # https://www.daleseo.com/python-heapq/
    # import heapq

# 우선순위 큐는 heapq로 만들어진 별도의 자료구조이다.
# heapq 모듈을 이용하면면 일반리스트를 최소힙처럼 쓸 수 있도록 한다.

# PriorityQueue 사용 코드

import sys
sys.stdin = open('input.txt')

from queue import PriorityQueue

que = PriorityQueue()

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        que.put(x)
    else:
        if que.empty():  # if que: 는 제대로 작동 안됨
            print(0)
        else:
            print(que.get())

