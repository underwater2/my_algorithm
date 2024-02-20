# deque 메서드
    # https://dongdongfather.tistory.com/72
    # insert(2, 'K')
    # remove('K')
    # reverse()

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for i in range(len(cities)):  # 도시 이름 모두 소문자로
        cities[i] = cities[i].lower()

    for city in cities:
        if city not in cache:
            answer += 5
            cache.appendleft(city)
            if len(cache) > cacheSize:
                cache.pop()
        else:
            answer += 1
            idx = cache.index(city)
            del cache[idx]
            cache.appendleft(city)
    return answer