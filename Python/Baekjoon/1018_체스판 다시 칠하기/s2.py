# s1에서 굳이 새 배열을 잘라 만들지 않고
# 행, 열 인덱스 합이 짝수인가 홀수인가 따지기

import sys
sys.stdin = open('input.txt')

def count(maps, i, j):
    global minN
    # 0,0 자리가 W일 때
    cntW = 0
    cntB = 0
    for n in range(i, i+8):
        for m in range(j, j+8):
            if (n+m) % 2:
                if maps[n][m] != 'B':
                    cntW += 1
                if maps[n][m] != 'W':
                    cntB += 1
            else:
                if maps[n][m] != 'W':
                    cntW += 1
                if maps[n][m] != 'B':
                    cntB += 1
    if min(cntW, cntB) < minN:
        minN = min(cntW, cntB)


N, M = map(int, sys.stdin.readline().split())

maps = [sys.stdin.readline().rstrip() for _ in range(N)]
minN = 987654321

for i in range(0, N-7):
    for j in range(0, M-7):
        count(maps, i, j)
print(minN)