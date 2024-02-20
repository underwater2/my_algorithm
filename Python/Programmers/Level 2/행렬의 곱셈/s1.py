def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):  # 행
        for j in range(len(arr2[0])):  # 열
            cnt = 0
            for c in range(len(arr2)):
                cnt += arr1[i][c] * arr2[c][j]
            answer[i][j] = cnt
    return answer