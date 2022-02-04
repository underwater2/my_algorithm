# 파이썬 SW문제해결 기본 - Stack2  3차시 03 분할정복
# 설명을 여러번 보면서 모든 경우의 수를 봐야지 이해가 가는 코드 같다.

def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)  # 순서가 결정된 a 리스트의 인덱스
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)


def partition(a, begin, end):  # a: 정렬할 리스트, begin: 맨처음 인덱스, end: 맨마지막 인덱스
    pivot = (begin + end) // 2  # 임시로 정한 pivot 값
    L = begin
    R = end
    while L < R:  # a 리스트의 길이가 1이면 정렬할 필요가 없다.
        while(a[L] < a[pivot] and L<R):  # L은 오른쪽으로 한 칸씩 이동하면서 pivot 값보다 크거나 같은 숫자를 찾는다.
            L += 1
        while(a[R] >= a[pivot] and L<R):  # R은 왼쪽으로 한 칸씩 이동하면서 pivot 값보다 작은 숫자를 찾는다.
            R -= 1
        if L < R:
            if L == pivot:  # L의 pivot 위치에 있고 R이 그 오른쪽에 있으면, 밑에서 둘 자리가 바뀐다.
                pivot = R  # 피봇 자리가 R과 교환되었으므로 피봇의 위치를 R로 확정지을 수 있음.
            a[L], a[R] = a[R], a[L]  # R과 L의 자리를 바꾼다.
    a[pivot], a[R] = a[R], a[pivot]  # L과 R이 같으면 피봇과 R자리가 바뀐다.
    return R
