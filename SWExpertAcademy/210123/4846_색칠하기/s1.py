import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list([0] * 10 for _ in range(10))
    count = 0  # 보라색 칸 수
    for n in range(N):  # 칠할 영역의 개수
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):  # 칠할 열 순회
            for c in range(c1, c2+1):  # 칠할 행 순회
                if arr[r][c] == 0:  # 아무것도 안칠해져있을 때
                    arr[r][c] = color  # 지금 색으로 칠하기
                if color == 1:  # 빨강색으로 칠하고있을 때
                    if arr[r][c] == 2:  # 파란색이 이미 칠해져있으면
                        arr[r][c] = 3  # 보라색으로 칠하기
                        count += 1  # 이거 없어서 오답 났었음!!
                if color == 2:  # 파란색으로 칠하고있을 때
                    if arr[r][c] == 1:  # 빨간색이 이미 칠해져있으면
                        arr[r][c] = 3  # 보라색으로 칠하기
                        count += 1  # 보라색 수 증가
                # 보라색으로 이미 칠해져있을 때는 아무것도 안함
    print('#{} {}'.format(tc, count))