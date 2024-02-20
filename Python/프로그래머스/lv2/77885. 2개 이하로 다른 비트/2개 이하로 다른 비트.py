def solution(numbers):
    answer = []
    for number in numbers:
        binary = bin(number)[2:]
        now, before = binary[-1], -1
        if now == '0':
            answer.append(int(binary[:-1] + '1', 2))
            continue
        for idx in range(len(binary)-2, -1, -1):
            before = now
            now = binary[idx]
            if now == '0':
                answer.append(int(binary[:idx] + '10' + binary[idx+2:], 2))
                break
        else:
            answer.append(int('10' + '1' * (len(binary)-1), 2))
    return answer