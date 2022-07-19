# 시간 초과 코드

import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    grade = [0 for _ in range(N+1)]
    for _ in range(N):
        doc, inv = map(int, sys.stdin.readline().split())
        grade[doc] = inv

    for i in range(1, N+1):
        if grade[i]:
            for j in range(i, N+1):
                if grade[i] < grade[j]:
                    grade[j] = 0
    cnt = 0
    for g in grade:
        if g:
            cnt += 1
    print(cnt)
