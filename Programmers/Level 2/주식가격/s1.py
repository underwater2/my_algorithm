# 스택
# 스택에 (인덱스, 가격)을 저장해놓고 가격이 내려간 것들을 pop 한다.
# '기간을 안적은 것들' 사이에 구멍처럼 '기간을 적은 것들'이 있다. 스택을 통해 '기간을 적은 것들'은 다시 볼 일이 없도록 한다.


from collections import deque

def solution(prices):
    stack = deque()
    answer = [0] * len(prices)
    # 가격이 내려갔을 때
    for i in range(len(prices)):
        if stack and prices[i] < stack[-1][1]:
            while stack and stack[-1][1] > prices[i]:
                temp = stack.pop()
                answer[temp[0]] = i-temp[0]
        stack.append((i, prices[i]))
    if stack:
        for s in stack:  # 마지막까지 가격이 안떨어진 것들
            answer[s[0]] = len(prices)-1-s[0]
    return answer