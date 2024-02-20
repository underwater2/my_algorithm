# meeting 배열을 뒤에서부터 순회하면 틀린다. 앞에서부터 순회해야 함
# 시작시간은 계속 늦어지고, 끝나는 시간이 빠를수록 좋으므로 이 점을 이용

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

meeting = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting = sorted(meeting)

start_time = meeting[0][0]
end_time = meeting[0][1]
result = 1
for i in meeting[1:]:
    if end_time <= i[0]:
        result += 1
        start_time = i[0]
        end_time = i[1]

    if end_time > i[1]:
        start_time = i[0]
        end_time = i[1]

print(result)