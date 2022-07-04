# 식을 세워서 풀었다
    # 낮에 올라가고 나서가 가장 빠르게 최고점에 도달할 수 있는 방법
    # \밤에 높이가 V-A보다 큰 가장 빠른 날을 찾으면, 그 다음 날에는 V에 도달하게 됨
import sys
sys.stdin = open('input.txt')

import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

goal = V-A
multi = A-B
ans = math.ceil(goal / multi)
print(ans+1)


#--------------------------------------------------------
# 시간초과 날 풀이
# 첫날부터 하루씩 계산하면서 올라가면 너무 많은 시간이 걸림
# (1 ≤ B < A ≤ V ≤ 1,000,000,000) : 조건 숫자가 너무 큼
# snail = 0
# day = 0
# while True:
#     day += 1
#     snail += A
#     if snail >= V:
#         print(day)
#         break
#     snail -= B