import sys
sys.stdin = open('input.txt')

N = int(input())
Pi = list(map(int, input().split()))

sort_Pi = sorted(Pi)
result = 0

for p in sort_Pi:
    result += p*N
    N -= 1
print(result)


