# 문자열
# 스택으로 풀었다

import sys
sys.stdin = open('input.txt')

from collections import deque

def test(ps):
    stack = deque()
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                    stack.pop()
            else:
                return 'NO'
    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'

T = int(input())

for tc in range(1, T+1):
    ps = input()
    print(test(ps))