def sequence(N):
    arr = [0 for _ in range(4)]
    idx = 0
    while N > 0:
        arr[idx] = N % 10
        N //= 10
        idx += 1

    first = True
    difference = 0
    for i in range(3, 0, -1):
        try:
            if arr[i] == 0 and first:
                continue
            if first:
                difference = arr[i] - arr[i-1]
                first = False
                continue
            if arr[i] - arr[i-1] != difference:
                return False
        except:
            return True
    return True

num = int(input())
result = 0
for i in range(1, num+1):
    if sequence(i):
        result += 1
print(result)

# sequence(109)

