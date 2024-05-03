def solution(genres, plays):
    gp = dict()
    maxgp = dict()
    for i in range(0, len(genres)):
        genrename = genres[i]
        # 장르 순서
        if genrename not in gp:
            gp[genrename] = plays[i]
        else:
            gp[genrename] += plays[i]
        # 장르별 노래 순서
        if genrename not in maxgp:
            maxgp[genrename] = [i]
        elif len(maxgp[genrename]) == 1:
            if plays[i] > plays[maxgp[genrename][0]]:
                maxgp[genrename].append(maxgp[genrename][0])
                maxgp[genrename][0] = i
            else:
                maxgp[genrename].append(i)
        else:
            if plays[i] > plays[maxgp[genrename][0]]:
                maxgp[genrename][1] = maxgp[genrename][0]
                maxgp[genrename][0] = i
            elif plays[i] > plays[maxgp[genrename][1]]:
                maxgp[genrename][1] = i

    sortgp = sorted(gp.items(), key=lambda x: x[1], reverse=True)

    answer = []

    for t in sortgp:
        answer.extend(maxgp[t[0]])

    return answer