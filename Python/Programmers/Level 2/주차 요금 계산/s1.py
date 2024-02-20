from collections import defaultdict
from math import ceil


def to_minute(time):
    t = time.split(':')
    return 60 * int(t[0]) + int(t[1])


def calc_fee(fees, times):
    total = 0
    for i in range(len(times) - 1, -1, -2):
        total += to_minute(times[i]) - to_minute(times[i - 1])
    if total <= fees[0]:
        return fees[1]
    else:
        return fees[1] + ceil((total - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    for record in records:
        data = record.split(' ')
        cars[data[1]].append(data[0])
    for car in sorted(cars.keys()):
        times = cars[car]
        if len(times) % 2:
            cars[car].append('23:59')
        answer.append(calc_fee(fees, cars[car]))
    return answer