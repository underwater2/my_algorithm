# 100보다 작은 셀프 넘버 찾기

def selfN(a):
    result = a
    while a > 0:
        result += a % 10
        a = a // 10
    return result

N = 10000
arr = [0 for _ in range(N+1)]

for i in range(1, N):
    j = i
    while True:
        selfNumber = selfN(j)
        if selfNumber > N:
            break
        j = selfNumber
        arr[selfNumber] = 1

for i in range(1, N+1):
    if arr[i] == 0:
        print(i)
