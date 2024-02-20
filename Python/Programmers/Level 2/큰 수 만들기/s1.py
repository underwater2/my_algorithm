# greedy 문제
# stack 풀이
# 풀이 참고: https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque

def solution(number, k):
    stack = deque()
    cnt = 0
    for num in number:
        while stack and stack[-1] < num and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num)
    if cnt != k:
        return ''.join(stack)[:-(k-cnt)]
    return ''.join(stack)