arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n):  # 1<<n 은 2^n과 같음. 이는 arr의 부분집합의 개수
    for j in range(n):  # (라이브에는 range(n+1)라고 나와있었는데, n이 정확한 것 같다) arr 원소의 수만큼 비트 자릿수를 비교
        if i & (1<<j):  # i의 j번째 비트가 1이면 j번쩨 원소 출력
            print(arr[j], end=", ")
    print()
print()

for i in range(1<<n):  # 1<<n 은 2^n과 같음. 이는 arr의 부분집합의 개수
    a = []
    for j in range(n):  # arr 원소의 수만큼 비트 자릿수를 비교
        if i & (1<<j):  # i의 j번째 비트가 1이면 j번쩨 원소 출력
            a.append(arr[j])
    print(a)
print()