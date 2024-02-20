# 스택/큐 문제
# deque의 rotate 메서드 사용

from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 1
    while True:
        maxIdx = queue.index(max(queue))
        if maxIdx == 0:
            if location == 0:
                return answer
            else:
                queue.popleft()
                location -= 1
                answer += 1
        else:
            queue.rotate(-maxIdx)
            location = (location + len(queue) - maxIdx) % len(queue)

    return answer