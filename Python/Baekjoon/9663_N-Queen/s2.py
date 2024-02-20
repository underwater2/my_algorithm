# deque도 써봄

import sys

def search(n):  # n은 0부터 N-1까지. 결정하는 행의 인덱스
    global N, cnt, queen
    if n == N:
        cnt += 1
        return
    for i in range(0, N):
        for q in queen:
            if (q[0] - n) == (q[1] - i) or -(q[0] - n) == (q[1] - i) or q[0] == n or q[1] == i:  # 대각선, 같은 행, 열 상에 있는지 확인
                break
        else:
            queen.append((n, i))
            search(n+1)
            queen.remove((n, i))



N = int(sys.stdin.readline())
queen = []
cnt = 0

search(0)
print(cnt)