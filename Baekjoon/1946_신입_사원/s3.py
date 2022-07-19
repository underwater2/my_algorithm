import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    grade = [0 for _ in range(N+1)]
    for _ in range(N):
        doc, inv = map(int, sys.stdin.readline().split())
        grade[doc] = inv

    cnt = 0
    minN = 100001
    for i in range(1, N+1):
        if minN > grade[i]:
            cnt += 1
            minN = grade[i]
    print(cnt)