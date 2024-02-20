import sys

N = int(sys.stdin.readline())

order = 0
for i in range(666, 987654321):
    for s in range(0, len(str(i))-2):  # 이 두 줄을 if "666" in str(i): 로 바꾸면
        if str(i)[s:s+3] == '666':     # 시간이 1/6배로 줄어든다..
            order += 1
            if order == N:
                print(i)
                exit()
            break

