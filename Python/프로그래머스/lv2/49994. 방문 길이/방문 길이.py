def solution(dirs):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    direction = {"U": 0, "D": 1, "R": 2, "L": 3}
    road = set()
    road_reverse = set()
    
    now = (0, 0)
    for d in dirs:
        after = (now[0] + dx[direction[d]], now[1] + dy[direction[d]])
        if -5 <= after[0] <= 5 and -5 <= after[1] <= 5:
            road.add((now, after))
            road_reverse.add((after, now))
            now = after
    duplication = len(road & road_reverse) // 2 
    return len(road) - duplication