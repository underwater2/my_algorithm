# raise Exception 빼먹어서 Fail 났었음

import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    eq = list(input().split())
    stack = deque()
    try:
        for e in eq:
            if e == '+':
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 + e2)
            elif e == '-':
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 - e2)
            elif e == '*':
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 * e2)
            elif e == '/':
                e2 = stack.pop()
                e1 = stack.pop()
                stack.append(e1 // e2)
            elif e == '.':  # eq 끝
                if len(stack) == 1:
                    print('#{} {}'.format(tc, stack.pop()))  # 답 출력
                else:  # eq가 끝나서 스택에 답 하나가 있어야 하는데, 2개 이상 숫자가 있으면
                    raise Exception  # 에러 만듦
            else:  # e가 숫자면
                stack.append(int(e))  # str을 int로 변환해서 stack에 넣음
    except:
        print('#{} {}'.format(tc, 'error'))  # eq가 잘못된 식일 경우 error 출력
