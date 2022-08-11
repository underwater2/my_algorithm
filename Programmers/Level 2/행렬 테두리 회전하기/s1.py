# while문 한 번에 한 칸씩만 저장, 이동해야 한다. 3칸씩 하면 테두리가 같은 수로 됐다.

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def solution(rows, columns, queries):

    answer = []
    # 행렬 만들기
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = ((i) * columns + j+1)

    def rotate(x1, y1, x2, y2):
        cnt = 0
        d = 0
        nx = x1  # 인덱스
        ny = y1
        minN = 987654321
        temp = arr[nx+1][ny]
        while cnt <= (2*(x2+y2-x1-y1)-1):
            cnt += 1

            if (nx, ny) in [(x1, y2), (x2, y2), (x2, y1)]:  # 방향 바꾸기
                d = (d+1) % 4

            newx = nx + dx[d]
            newy = ny + dy[d]

            if arr[nx][ny] < minN:
                minN = arr[nx][ny]

            temp1 = arr[nx][ny]  # 다음 위해 저장
            arr[nx][ny] = temp
            temp = temp1
            nx, ny = newx, newy
        answer.append(minN)

    # 회전하기
    for que in queries:
        rotate(que[0]-1, que[1]-1, que[2]-1, que[3]-1)
    return answer