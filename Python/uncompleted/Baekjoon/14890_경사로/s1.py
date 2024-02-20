import sys
sys.stdin = open('input.txt')

# 길을 한 방향으로 순회 -> 받침대 있는 자리를 1로 한 N*N 배열 생성 -> 반대편 방향으로 순회하면서 받침대 겹치면 그만
def walk():
    for i in range(N):
        height = 0
        length = 1
        for j in range(N):
            # 행 순회
            if not height:
                height = maps[i][j]
            else:
                if height == maps[i][j]:
                    length += 1
                else:  # 다른 높이를 만났을 때
                    if height + 1 == maps[i][j]:  # 한 칸 높은 곳을 만남
                        if length >= L:  # 받침대가 놓일 길이가 될 때
                            height = 0
                            length = 1
                        else:
                            break  # => 이 행은 그만 봄
                    # elif height - 1 == maps[i][j]:  # 한 칸 낮은 곳을 만남
                    else:  # 높이 차가 1보다 크다 => 이 행은 그만 봄
                        break

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(N, L)
    walk()
