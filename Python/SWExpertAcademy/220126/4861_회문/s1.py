import sys
sys.stdin = open('sample_input.txt')

def is_palindrome(s):  # s: 검사하고싶은 문자열
    len_s = len(s)
    result = 0  # 0이면 회문 아님, 1이면 회문 맞음
    # 문자열 길이가 홀수, 짝수일 때 구분 안해도 됨
    for i in range(len_s // 2):  # 홀수일 때, 정가운데 혼자 남는 문자는 검사 x
        if s[i] != s[len_s-1-i]:
            break
    else:
        result = 1
    return result

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]  # 가로회문 검사용
    # 세로로 읽은 문자열을 가로로 읽을 수 있게 만들기 (행, 열을 반대로)
    arr2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[j][i]
    for i in range(N):
        arr2[i] = ''.join(arr2[i])

    result = ''

    # 가로, 세로 순회
    j = 0
    while result == '' and j < N:
        for i in range(N-M+1):
            # 가로
            if is_palindrome(arr[j][i:M+i]):  # 회문이면
                result = arr[j][i:M+i]
                break
            # 세로
            if is_palindrome(arr2[j][i:M+i]):  # 회문이면
                result = arr2[j][i:M+i]
                break
        j += 1

    print('#{} {}'.format(tc, result))