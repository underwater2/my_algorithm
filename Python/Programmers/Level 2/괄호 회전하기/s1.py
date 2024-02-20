# 회전할 때 마다 rotate 해주고 stack 이용해 올바른 괄호 문자열인지 판단함
# 일반 괄호 문제에 회전 개념만 넣어서 완전탐색한 문제
    # 따로 규칙을 찾아야 하는 문제가 아니었다


from collections import deque

def solution(s):
    que = deque(list(s))
    que.rotate(1)
    stack = deque()
    answer = 0
    for _ in range(len(s)-1):
        stack.clear()
        que.rotate(-1)
        for q in que:
            if q in ('{', '[', '('):
                stack.append(q)
            else:
                try:
                    next = stack.pop()
                    if (q == '}' and next != '{') or (q == ']' and next != '[') or (q == ')' and next != '('):
                        break
                except:  # 스택이 비어있을 경우
                    break
        else:
            if stack:
                break
            else:
                answer += 1
    return answer