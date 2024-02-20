def solution(arr):
    arr.sort()
    largeN = arr[-1]
    x = 1
    while True:
        for i in range(len(arr)-1):
            if (largeN*x) % arr[i] != 0:
                x += 1
                break
        else:
            return largeN*x