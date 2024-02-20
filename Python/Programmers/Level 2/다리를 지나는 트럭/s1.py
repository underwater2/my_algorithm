# 큐 문제
# 풀이 과정
    # 큐 사용법 힌트 얻음
        # 0으로 도로의 공백을 채운다.
        # 참고: https://school.programmers.co.kr/questions/16250
    # 풀이중 5번 시간초과
        # 다리 위에 있는 트럭의 무게 합을 계산하는 sum() 때문이었다. 시간복잡도 O(N)
        # 별도의 변수(w)를 만들어서 계산하니 40배 정도 빨라졌다...
        # 참고: https://school.programmers.co.kr/questions/19667


from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    sec = 0
    w = 0  # 다리 위에 있는 트럭의 무게 합
    while True:
        sec += 1
        if not truck and w == 0:
            break
        out_truck = bridge.popleft()
        w -= out_truck
        if truck and (w + truck[0]) <= weight:
            next_truck = truck.popleft()
            w += next_truck
            bridge.append(next_truck)
        else:
            bridge.append(0)
    return sec-1