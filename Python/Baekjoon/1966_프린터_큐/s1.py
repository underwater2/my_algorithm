# 다른 풀이
# https://hongcoding.tistory.com/42

import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    docs = deque(list(map(int, sys.stdin.readline().split())))
    flag = 1
    cnt = 0

    while flag:
        top = docs[0]
        maxIdx = 0
        maxN = docs[maxIdx]
        # 뒤에 최댓값 있는지 찾기
        for i in range(1, len(docs)):
            if maxN < docs[i]:
                maxN = docs[i]
                maxIdx = i
        if maxN != 0:
            docs.rotate(-maxIdx)
            M = M - maxIdx if (M - maxIdx >= 0) else len(docs) + (M - maxIdx)
        if M == 0:
            flag = 0
        docs.popleft()
        cnt += 1
        M -= 1
    print(cnt)

