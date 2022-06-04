# 브루트 포스

def program(N):
    for i in range(1, N):
        result = i
        for j in str(i):
            result += int(j)
        if result == N:
            return i
    return 0

N = int(input())
print(program(N))
