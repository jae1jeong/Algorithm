
from collections import deque
def solution(cacheSize, cities):
    ans = 0
    cache = deque()
    cities = [city.lower() for city in cities]
    
    for city in cities:
        if city in cache:
            ans += 1                
            cache.remove(city)
            cache.append(city)

        else:
            ans += 5
            if cacheSize > len(cache):
                cache.append(city)
            
            elif cacheSize == 0:
                continue
            else:
                cache.popleft()
                cache.append(city)
    return ans

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cs = 3

ct = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cs = 3

ct =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cs = 2

ct = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cs = 5

ct =["Jeju", "Pangyo", "NewYork", "newyork"]
ct = [city.lower() for city in ct]
cs = 2
print(solution(cs,ct))
ct = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cs = 0
