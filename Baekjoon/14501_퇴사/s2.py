# dfs로 해결
# 검색해보니 dp(동적계획법)으로 풀었다는 얘기가 많았다.
    # 아래 코드 참고
    # https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-exjyfr5vgj

import sys
sys.stdin = open('input.txt')

def dfs(start):
    global amount, result

    if start + tp[start][0] <= N+1:
        amount += tp[start][1]  # 더하기 전에, 유효한 값인지 확인해야할듯
    result = max(amount, result)
    for i in range(start + tp[start][0], N+1):
        if i + tp[i][0] <= N+1:
            dfs(i)
            amount -= tp[i][1]


N = int(sys.stdin.readline())

tp = [0]
for _ in range(N):
    tp.append(list(map(int, sys.stdin.readline().split())))

res = 0

for i in range(1, N+1):
    amount, result = 0, 0
    dfs(i)
    res = max(res, result)

print(res)