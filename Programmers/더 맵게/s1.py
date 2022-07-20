# 최소힙: heapq 사용해야 통과된다고 한다
# scoville 리스트를 힙으로 변환하고 시작해야 한다.
    # heap 안의 모든 원소들은 heappush로 넣는다.
    # 이미 리스트가 있다면 통째로 힙으로 변환(heapify)한다.

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        min2 = heapq.heappop(scoville)
        newS = min1 + (min2 * 2)
        heapq.heappush(scoville, newS)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1