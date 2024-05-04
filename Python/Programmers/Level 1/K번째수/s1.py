def solution(array, commands):
    answer = []
    for command in commands:
        newarr = sorted(array[command[0]-1:command[1]])
        answer.append(newarr[command[2]-1])
    return answer
