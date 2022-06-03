# 재귀?
import sys

def search(n):  # n은 0부터 N-1까지. 결정하는 행의 인덱스
    global N, cnt, queen
    if n == N:
        cnt += 1
        return
    for i in range(0, N):
        for idx in range(0, n):
            if (queen[0][idx] - n) == (queen[1][idx] - i) or -(queen[0][idx] - n) == (queen[1][idx] - i) or queen[0][idx] == n or queen[1][idx] == i:  # 대각선, 같은 행, 열 상에 있는지 확인
                break
        else:
            queen[0][n], queen[1][n] = n, i
            search(n+1)
            queen[0][n], queen[1][n] = 0, 0



N = int(sys.stdin.readline())
queen = [[0]*N for _ in range(2)]
cnt = 0

search(0)
print(cnt)