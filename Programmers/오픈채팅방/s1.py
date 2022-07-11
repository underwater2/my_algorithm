def solution(record):
    ids = dict()
    for rec in record:
        data = rec.split()
        if data[0] in ["Enter", "Change"]:
            ids[data[1]] = data[2]

    answer = []
    for rec in record:
        data = rec.split()
        if data[0] == "Enter":
            message = ids[data[1]] + "님이 들어왔습니다."
        elif data[0] == "Leave":
            message = ids[data[1]] + "님이 나갔습니다."
        else:
            continue
        answer.append(message)

    return answer
