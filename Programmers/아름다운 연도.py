def beautiful(year):
    year = list(str(year))
    length = len(year)
    if len(set(year)) == length:
        return True
    return False 


def solution(p):   
    for idx in range(len(years)):
        if int(years[idx]) == p:
            return int(years[idx+1])

years = []
for year in range(1000,10001):    
    if beautiful(year):
        years.append(year)
