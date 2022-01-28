# deque를 사용했는데 runtime error가 떴었다.
# 그래서 테스트케이스에 아무렇게나 만들어서 돌렸더니 에러가 떴음
# -> stack에서 열린괄호를 찾아야하는데 pop될 요소가 없으면 에러난다.

import sys
sys.stdin = open('sample_input.txt')

import collections

def checking(code):
    stack = collections.deque()
    for c in code:  # 문장을 순회하면서 {, }, (, ) 만 걸러냄
        if c in ['{', '(']:  # 1. 열린괄호일때는 스택에 추가
            stack.append(c)
        elif c in ['}', ')']:  # 2. 닫힌 괄호일 때는 스택의 끝쪽에 같은 짝의 열린괄호가 있는지 확인해야함
            if not stack:  # pop 해야하는데 스택이 비어있으면 0반환
                return 0
            else:
                s = stack.pop()
                if (s, c) == ('{', ')') or (s, c) == ('(', '}'):  # 짝이 안맞으면 0반환
                    return 0
    if stack:  # 3. 문장 순회를 끝냈는데 스택에 열린괄호가 남아있으면 0반환
        return 0
    return 1  # 위에서 아닌 경우를 다 걸러서 1반환

T = int(input())

for tc in range(1, T+1):
    code = input()
    print('#{} {}'.format(tc, checking(code)))
