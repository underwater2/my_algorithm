# 처음에 Recursion errer가 떴었다
    # 아래 코드 한 줄 추가로 해결
    # sys.setrecursionlimit(100000)
        # https://thing-u.tistory.com/47
            # DFS로 풀다가 recursion error 가 떠서 기록해둔다.
            # 파이썬에서는 1000번 이상의 recursion이 발생하면 recursion error 가 뜬다.
            # 그럴땐 아래코드를 추가해서 해결하면된다.
            # O(n^3) 이기도하고 row, col이 각각 100 이면 최대 10000번의 재귀가 발생한다.

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)

def left(r, c, d):
    if d == 0:
        c -= 1
    elif d == 1:
        r -= 1
    elif d == 2:
        c += 1
    else:
        r += 1
    return r, c

def back(r, c, d):
    if d == 0:
        r += 1
    elif d == 1:
        c -= 1
    elif d == 2:
        r -= 1
    else:
        c += 1
    return r, c

N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(r, c, d, cnt):
    lr, lc = left(r, c, d)
    if maps[lr][lc] == 0:
        d = (d + 3) % 4
        return cleaning(lr, lc, d)
    else:
        if cnt != 4:
            d = (d + 3) % 4
            return rotate(r, c, d, cnt+1)
        else:
            # 뒤쪽이 벽이면
            br, bc = back(r, c, d)
            if maps[br][bc] == 1:
                return
            else:
                return rotate(br, bc, d, 0)

# 1번
def cleaning(r, c, d):
    maps[r][c] = 2

    return rotate(r, c, d, 0)


cleaning(r, c, d)

ans = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            ans += 1
print(ans)