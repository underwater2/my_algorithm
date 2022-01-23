import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus = list(map(int, input().split()))
    bus.insert(0, 0)  # bus list 맨앞에 출발지 0을 추가
    bus.append(N)  # bus list 맨뒤에 목적지 N을 추가

    # 뒤에서부터 가기
    count = 0  # 거쳐간 정류장 수
    now = len(bus) - 1  # 도착 지점(인덱스)에서 시작
    while now != 0:
        for i in range(now-1, -1, -1):  # 현재지점의 앞 인덱스부터 역순으로 순회
            if bus[now] <= K:  # 현재 위치가 K보다 작아서 더이상 정류장을 들릴 필요 없을 때
                now = 0  # while 문을 끝냄
                break  # for문 바로 밑의 if문에서 break 하면 while조건문으로 넘어감
            if bus[now] - bus[i] <= K:  # 현재 위치와 도착한 곳의 거리 차이가 K보다 작거나 같을 때
                continue  # 거리 차이가 가장 큰 곳을 선택해야하므로 일단 한 칸 더 순회
            elif now == i+1:  # now에서 한 칸 밖에 이동하지 않았는데 서로의 거리가 K보다 클 때
                now = 0  # 불가능한 케이스이므로 while문 끝내고 0을 출력한다
                count = 0
                break
            else:  # 서로의 거리가 K를 넘지 않으면서, 가장 멀리 앞으로 갈 수 있는 곳을 선택
                now = i+1  # i+1 인덱스부터 거리가 K를 안넘음
                count += 1  # 정류장 선택하므로 count 증가
                break
    print('#{} {}'.format(tc, count))

