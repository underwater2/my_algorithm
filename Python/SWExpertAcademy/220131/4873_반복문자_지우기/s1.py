# stack 칸에 있길래 stack으로 풀었다. 수업에서는 string slicing으로 풀었음.
# 삽질하다가 생각나는대로 적었더니 풀렸다...
# 일단 stack에 넣어놓으면 stack[-1] 이랑만 매번 비교하면 되니까 코드가 짧아진 것 같다.

import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    string = input()  # string으로 받음
    stack = deque()  # deque 생성

    for s in range(len(string)):  # 문자열의 인덱스 0부터 끝까지 순회
        if stack:  # 스택이 비어있지 않으면
            if stack[-1] != string[s]:  # 스택의 맨 바깥쪽 문자와 문자열의 현재 위치 문자가 안겹치면
                stack.append(string[s])  # stack에 문자 추가
            else:  # 스택의 맨 바깥쪽 문자와 문자열의 현재 위치 문자가 똑같으면
                stack.pop()  # 겹치는 문자를 stack에서 제거
        else:  # 스택이 비어있으면
            stack.append(string[s])  # 문자를 추가

    print('#{} {}'.format(tc, len(stack)))  # 남은 stack의 문자들이 몇개인지 출력


    # while문 안의 while문...
    # s = 0
    # while s < len(string)-1:
    #     if string[s] != string[s+1]:
    #         stack.append(string[s])
    #         s += 1
    #     else:
    #         if string[s+2] != stack[-1]:
    #             s += 2
    #         else:
    #             stack.pop()
    #             if string[s + 3] != stack[-1]:
    #                 s += 3
    #             else:
    #                 stack.pop()

