# 하드코딩해서 풀었다.
# 함수 내부에 함수를 넣었다.

def solution(places):
    def inspect(i, j, cnt):
        # 십자모양 검사
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 2), (2, 0), (0, -2), (-2, 0)]
        part = [0] * 4
        for idx, t in enumerate(dxdy):
            if 0 <= i + t[0] < 5 and 0 <= j + t[1] < 5:
                state = places[cnt][i + t[0]][j + t[1]]
                if state == 'P':
                    if idx < 4:
                        return False
                    else:
                        if places[cnt][i + dxdy[idx - 4][0]][j + dxdy[idx - 4][1]] == 'O':
                            return False
                if idx < 4 and state == 'X':
                    part[idx] = 1

        # 대각선 검사
        dxdy2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for idx2, t2 in enumerate(dxdy2):
            if 0 <= i + t2[0] < 5 and 0 <= j + t2[1] < 5:
                state = places[cnt][i + t2[0]][j + t2[1]]
                if state == 'P':
                    if idx2 == 0:
                        if part[0] != 1 or part[1] != 1:
                            return False
                    elif idx2 == 1:
                        if part[1] != 1 or part[2] != 1:
                            return False
                    elif idx2 == 2:
                        if part[2] != 1 or part[3] != 1:
                            return False
                    elif idx2 == 3:
                        if part[3] != 1 or part[0] != 1:
                            return False
        # 처음에 places의 내부 문자열을 한글자씩 떼서 list화 시켰어야 가능하다.
        # places[cnt][i][j] = 'O'
        return True

    answer = [1] * 5
    for cnt, place in enumerate(places):
        flag = 0   # 이중 for문 탈출 위한 flag
        for i, r in enumerate(place):
            for j, c in enumerate(r):
                if c == 'P':  # 주변 P 검사
                    if not inspect(i, j, cnt):
                        answer[cnt] = 0
                        flag = 1
                        break
            if flag:
                break

    return answer
