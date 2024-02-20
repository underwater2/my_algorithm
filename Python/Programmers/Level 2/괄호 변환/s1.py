# 문제에 제시된 알고리즘대로 재귀 구현하면 풀리는 문제

from collections import deque


def correct(p):  # 올바른 괄호 문자열인지 판단
    stack = deque()
    for s in p:
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                return False
    if stack:
        return False
    return True


def divide(p):  # u와 v를 분리하는 idx 위치 반환
    cnt = 0
    idx = 0
    for s in p:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx
        idx += 1


def reverse(p):  # (, )를 반대로 반환
    result = ""
    for s in p:
        if s == "(":
            result += ")"
        else:
            result += "("
    return result


def solution(p):
    if not p:
        return ""

    if correct(p):
        return p
    else:
        idx = divide(p)
        u = p[:idx + 1]
        v = p[idx + 1:]
        if correct(u):
            return u + solution(v)
        else:
            result = "(" + solution(v) + ")" + reverse(u[1:len(u) - 1])
            return result

    answer = ''
    return answer