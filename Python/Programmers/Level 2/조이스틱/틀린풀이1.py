# 그리디 접근: 같은 거리인 알파벳이 있을 때, 재귀로 두 경우 다 탐색해야 한다.
    # 13, 23, 25번 실패
    # 반례: "BBBBAAAABA" 12
    # 해당 접근법으로는 정확한 답이 나오지 않는다.

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
        print('now', now)
        print('distance', distance)
        # 최소 거리인 idx 구하기
        minN = min(distance)
        for idx, dist in enumerate(distance):
            if dist == minN:  # 거리가 같은 경우는? 반례 "ABAAAAAAAAABB"
                move(visit[idx], moving + minN, visit[:idx] + visit[idx + 1:])

    cnt = [0] * len(name)
    for idx, char in enumerate(name):
        temp = ord(char) - 65
        if temp > 13:
            temp = 26 - temp
        cnt[idx] = temp
    if 0 not in cnt:
        return sum(cnt) + len(name) - 1
    elif sum(cnt) == 0:
        return 0
    else:
        # 최소이동거리인 1을 매번 찾고 거기로 이동한다
        visit = []
        for idx, c in enumerate(cnt):
            if c and idx:
                visit.append(idx)
        # 재귀
        now = 0
        moving = 0
        move(now, moving, visit)
    return sum(cnt) + answer
