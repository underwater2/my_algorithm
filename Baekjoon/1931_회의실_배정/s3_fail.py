# 틀렸습니다

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
if N == 1:
    print(1)
else:
    meeting = []
    for i in range(N):
        start, end = map(int, sys.stdin.readline().split())
        meeting.append((start, end))

    meeting = sorted(meeting, key=lambda x:x[1])
    print(meeting)
    result = 0
    cnt = 1
    temp = meeting[-1]
    for i in range(N-2, -1, -1):

        if temp[1] == meeting[i][1]:
            if temp[0] < meeting[i][0]:
                temp = meeting[i]
                cnt = 1
            elif temp[0] == meeting[i][0]:
                cnt += 1
        elif temp[1] > meeting[i][1]:
            if temp[0] >= meeting[i][1]:
                result += cnt
                cnt = 1
                temp = meeting[i]
            elif temp[0] <= meeting[i][0]:
                temp = meeting[i]
                cnt = 1
            # elif temp[0] < meeting[i][1]:
            #     temp = meeting[i]
        if i == 0:
            result += cnt
            cnt = 1
    print(result)
