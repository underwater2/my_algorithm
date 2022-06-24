# 틀린 코드

import sys
sys.stdin = open('input.txt')

def calc():
    if N == 1:
        return cards[0]
    else:
        nums = cards[0] + cards[1]
        ans = nums
        for i in range(2, N):
            ans += nums + cards[i]
            nums += cards[i]
        return ans

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cards = sorted(cards)
print(calc())