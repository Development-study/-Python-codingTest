# 카카오 2018 공채 문제 3번
# 캐시 (난이도 : 하)

from collections import deque

def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYrok', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution(cacheSize, cities))