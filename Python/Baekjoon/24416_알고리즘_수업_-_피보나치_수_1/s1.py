# 문제 해설 참고: https://justduke.tistory.com/146

# pypy3으로 제출해야함. python3으로 제출하면 시간초과 난다.

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())

def fib_recursion(n):
    global cnt_rec
    if n == 1 or n == 2:
        return 1
    else:
        cnt_rec += 1
        return (fib_recursion(n-1) + fib_recursion(n-2))


def fib_dp(n):
    global cnt_dp
    fib_nums = [0] * 41
    fib_nums[1], fib_nums[2] = 1, 1
    for i in range(3, n+1):
        cnt_dp += 1
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
    return fib_nums[n]

cnt_rec = 0
cnt_dp = 0
fib_recursion(n)
fib_dp(n)
print(cnt_rec+1, cnt_dp)
