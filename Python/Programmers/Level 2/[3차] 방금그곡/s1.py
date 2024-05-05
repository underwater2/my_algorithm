from collections import deque

def solution(m, musicinfos):
    poss = []
    idx = -1 # 곡 순서
    for musicinfo in musicinfos:
        idx += 1
        # 분 세기
        rtime = 0
        info = musicinfo.split(',')
        sh, sm = int(info[0][:2]), int(info[0][3:])
        eh, em = int(info[1][:2]), int(info[1][3:])
        if em >= sm:
            rtime = (em - sm) + (eh - sh) * 60
        else:
            rtime = (60 + em - sm) + (eh - sh - 1) * 60
        
        # 노래 음별로 나누기
        music = info[3]    
        marr = deque()
        i = len(music)-1
        while i >= 0:
            if music[i] == '#':
                marr.appendleft(music[i-1:i+1])
                i -= 2
            else:
                marr.appendleft(music[i:i+1])
                i -= 1
        if marr[0] == ' ':
            marr.popleft()
        
        # 노래 반복하기        
        fullmusic = music * (rtime // len(marr)) + ''.join(list(marr)[0: (rtime % len(marr))])
        
        # 일치하는지 확인
        if m[-1] == '#':
            if fullmusic.find(m) != -1:
                poss.append((rtime, idx, info[2]))
        else:
            if fullmusic.count(m) != fullmusic.count(m + '#'):
                poss.append((rtime, idx, info[2]))
    
    # 가능성있는 곡들중 선택
    select = sorted(poss, key=lambda x: (-x[0], x[1]))
        
    answer = ''
    if select:
        answer = select[0][2]
    else:
        answer = "(None)"
    return answer
