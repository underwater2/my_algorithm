# 3차원 배열에 memoization 하기
# 재귀 함수 구조 자체는 남겨두고 매번 memo한 값이 있는지 확인해가는 방법으로 풀었다.

# 입력으로 테스트 케이스의 개수가 주어지지 않으므로 EOF를 판단해서 프로그램을 종료해야 합니다
# 문자열을 입력받아 EOF(End Of File; 파일의 끝)를 판단할 수 있는지
    # https://y00n-lee.tistory.com/9

import sys
sys.stdin = open('input.txt')

def search_memo(x, y, z):
    if wN[x][y][z]:
        return wN[x][y][z]
    else:
        return w(x, y, z)

def w(a, b, c):

    if wN[a][b][c]:
        return wN[a][b][c]

    elif a > 70 or b > 70 or c > 70:
        return search_memo(70, 70, 70)

    elif a < b < c:
        r1, r2, r3 = 0, 0, 0
        r1 = search_memo(a, b, c-1)
        r2 = search_memo(a, b-1, c-1)
        r3 = search_memo(a, b-1, c)
        wN[a][b][c] = r1 + r2 - r3
        return r1 + r2 - r3

    else:
        r1, r2, r3, r4 = 0, 0, 0, 0
        r1 = search_memo(a-1, b, c)
        r2 = search_memo(a-1, b-1, c)
        r3 = search_memo(a-1, b, c-1)
        r4 = search_memo(a-1, b-1, c-1)
        wN[a][b][c] = r1 + r2 + r3 - r4
        return r1 + r2 + r3 - r4


wN = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
for a in range(0, 51):
    for b in range(0, 101):
        for c in range(0, 101):
            wN[a][b][c] = 1
            wN[b][a][c] = 1
            wN[c][b][a] = 1


while True:
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    if x != -1 or y != -1 or z != -1:
        print(f'w({x}, {y}, {z}) = {w(x+50, y+50, z+50)}')
    else:
        break