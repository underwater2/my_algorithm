# in 이나 not in은 최악에 경우에는 O(n)에 시간이 걸릴수 있다.

import sys
sys.stdin = open('input.txt')

from collections import deque

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

def calc(num):
    temp = deque()
    nowN = 1
    pp = deque()

    for i in num:
        if i >= nowN:
            for j in range(nowN, i):
                temp.append(nowN)
                nowN += 1
                pp.append('+')
            nowN += 1
            pp.append('+')
            pp.append('-')
        else:
            outN = temp.pop()
            pp.append('-')
            if outN != i:
                pp = ['NO']
                return pp
    return pp


for p in calc(num):
    print(p)