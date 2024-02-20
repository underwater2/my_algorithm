# 스택/큐

import math
from collections import deque

def solution(progresses, speeds):

    times = deque([0] * len(speeds))
    for i in range(len(speeds)):  # 완료까지 얼마나 남았는지 계산해서 times 배열에 넣는다
        times[i] = math.ceil((100-progresses[i])/speeds[i])

    now = times[0]
    day = 1
    times.popleft()
    answer = []
    for t in times:
        if t <= now:
            day += 1
        else:
            now = t
            answer.append(day)
            day = 1
    if day:
        answer.append(day)
    return answer