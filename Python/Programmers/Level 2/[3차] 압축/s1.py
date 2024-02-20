def solution(msg):
    answer = []
    index = dict()
    for i in range(65, 91):
        index[chr(i)] = i - 64
    num = 26
    i = 0
    while i < len(msg):
        for j in range(i + 2, len(msg) + 1):
            if msg[i:j] not in index:
                answer.append(index[msg[i:j - 1]])
                num += 1
                index[msg[i:j]] = num
                i += (j - i - 1)
                break
        else:
            answer.append(index[msg[i:]])
            break
        print(index)

    # print(ord('A'))
    # print(chr(90))  # Z
    return answer