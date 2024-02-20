import sys
sys.stdin = open('input.txt')

def count(maps, a, b):
    global minN
    # 0,0 자리가 W일 때
    cnt = 0
    for n in range(8):
        if n in [0, 2, 4, 6]:
            for m in range(8):
                if m in [0, 2, 4, 6]:
                    if maps[n][m] != a:
                        cnt += 1
                else:
                    if maps[n][m] != b:
                        cnt += 1
        else:
            for m in range(8):
                if m in [0, 2, 4, 6]:
                    if maps[n][m] != b:
                        cnt += 1
                else:
                    if maps[n][m] != a:
                        cnt += 1
    if cnt < minN:
        minN = cnt
    # 0,0 자리가 B일 때


N, M = map(int, sys.stdin.readline().split())

maps = [sys.stdin.readline().rstrip() for _ in range(N)]
minN = 987654321

for i in range(0, N-7):
    for j in range(0, M-7):
        # 8x8로 자른 새로운 배열 만들기
        newMap = []
        for k in range(8):
            newMap.append(maps[i+k][j:j+8])
        count(newMap, 'W', 'B')
        count(newMap, 'B', 'W')
print(minN)