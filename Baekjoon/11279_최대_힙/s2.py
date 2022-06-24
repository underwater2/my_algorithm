# PriorityQueue 사용 코드

import sys
sys.stdin = open('input.txt')

from queue import PriorityQueue

que = PriorityQueue()

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        que.put(-x)
    else:
        if que.empty():  # if que: 는 제대로 작동 안됨
            print(0)
        else:
            print(-que.get())