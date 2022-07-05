# 인덱스 에러가 계속 났었다.
    # n 입력이 2이상 숫자라고 써있지만 1이 입력될 경우도 고려해서 에러 안나게 해야함...

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

for i in range(2, n+1):
    minN = []
    if i % 3 == 0:
        minN.append(1 + dp[i//3])
    if i % 2 == 0:
        minN.append(1 + dp[i//2])
    minN.append(1 + dp[i-1])
    dp[i] = min(minN)

print(dp[n])