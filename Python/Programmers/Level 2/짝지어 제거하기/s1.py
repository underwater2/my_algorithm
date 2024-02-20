# 스택 문제
    # 문자열 말고 스택으로 푸니 너무 간단하게 풀렸다.

from collections import deque

def solution(s):
    if len(s) % 2:  # 문자열 길이는 짝수여야함
        return 0

    stack = deque()
    answer = 1
    for al in s:
        if stack:
            if stack[-1] == al:
                stack.pop()
            else:
                stack.append(al)
        else:
            stack.append(al)
    print(list(stack))
    if stack:
        return 0

    return answer