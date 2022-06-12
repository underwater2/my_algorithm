import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A = sorted(A)
B = sorted(B, reverse=True)
result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)