# 블록 내리기 로직이 어려웠다.

from collections import deque

def search(m, n, board, note):
    # 4칸 검색
    for i in range(m-1):
        for j in range(n-1):
            now = board[i][j]
            if now != '0':
                if board[i+1][j] == now and board[i][j+1] == now and board[i+1][j+1] == now:
                    note[i][j], note[i+1][j], note[i][j+1], note[i+1][j+1] = '0', '0', '0', '0'
    # 재귀 탈출 -> 삭제된 블록이 없을 때
    if board == note:
        # 지워진 칸 세기
        answer = 0
        for i in range(m):
            for j in range(n):
                if note[i][j] == '0':
                    answer += 1
        return answer
    # 블록 내리기
    for j in range(n):
        blank = -1
        block = deque()
        for i in range(m-1, -1, -1):
            if blank < 0 and note[i][j] == '0':
                blank = i
            if blank >= 0 and note[i][j] != '0':
                block.append((i,j))
        for k in range(blank, blank-len(block), -1):
            a, b = block.popleft()
            note[k][j] = note[a][b]
            note[a][b] = '0'
    board = [n[:] for n in note]  # 깊은 복사
    return search(m, n, board, note)


def solution(m, n, pre_board):
    board = [list(b) for b in pre_board]
    note = [b[:] for b in board]  # 깊은 복사
    return search(m, n, board, note)