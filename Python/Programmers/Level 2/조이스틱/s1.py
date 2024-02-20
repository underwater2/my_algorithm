# 표기는 그리디지만 완전탐색으로 해결해야하는 문제
# 풀이 과정
    # 그리디 접근: 최소이동거리인 알파벳을 매번 찾고 거기로 이동한다. 반복
        # 반례: "ABAAAAAAAAABB" 4
    # 그리디 접근: 같은 거리인 알파벳이 있을 때, 재귀로 두 경우 다 탐색해야 한다.
        # 13, 23, 25번 실패
        # 반례: "BBBBAAAABA" 12
        # 해당 접근법으로는 정확한 답이 나오지 않는다.
    # 완전탐색
        # 정답
        # 최소이동거리가 아닌 모든 경우를 재귀로 완전탐색


answer = 987654321

def solution(name):
    def move(now, moving, visit):
        global answer
        # 탐색 완료
        if not visit:
            if moving < answer:
                answer = moving
            return
        # 거리 재기
        distance = [0] * len(visit)
        for idx, v in enumerate(visit):
            temp = abs(v - now)
            if temp > len(cnt) // 2:
                temp = len(cnt) - temp
            distance[idx] = temp
        # 순회하기
        for idx, dist in enumerate(distance):
            move(visit[idx], moving + distance[idx], visit[:idx] + visit[idx + 1:])

    cnt = [0] * len(name)  # cnt: 알파벳 만들기 위한 위, 아래 이동 횟수의 리스트
    for idx, char in enumerate(name):
        temp = ord(char) - 65
        if temp > 13:
            temp = 26 - temp
        cnt[idx] = temp
    if 0 not in cnt:  # 만들 알파벳에 A가 없을 때 (이동순서가 정해져있다)
        return sum(cnt) + len(name) - 1
    elif sum(cnt) == 0:  # 만들 알파벳이 모두 A인 경우
        return 0
    else:  # 이동 순서를 모두 탐색해야할 때
        visit = []  # 방문해야하는 인덱스들의 리스트
        for idx, c in enumerate(cnt):
            if c and idx:
                visit.append(idx)
        # 재귀로 완전탐색
        now = 0  # 현재 위치 인덱스
        moving = 0  # 이동 횟수의 총합
        move(now, moving, visit)
    return sum(cnt) + answer
