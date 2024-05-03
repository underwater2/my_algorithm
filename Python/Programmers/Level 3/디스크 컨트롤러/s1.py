import heapq

def solution(jobs):
    sjobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    count = len(sjobs)
    h = []
    now = 0
    answer = 0
    while sjobs:
        while sjobs[-1][0] <= now:
            heapq.heappush(h, sjobs.pop()[::-1])
            if not sjobs:
                break
        if h:
            req = heapq.heappop(h)
            now += req[0]
            answer += now - req[1]
        else:
            now += 1
    while h:
        req = heapq.heappop(h)
        now += req[0]
        answer += now - req[1]

    answer = answer//count

    return answer