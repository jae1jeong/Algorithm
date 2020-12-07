from collections import defaultdict

def solution(genres, plays):
    answer = []
    albums = defaultdict(lambda:[])
    index = 0
    albumCounts = defaultdict(int)
    
    for genre,play in zip(genres,plays):
        albums[genre].append((index,play))
        albumCounts[genre] += play
        index += 1
    
    sorted_genres = sorted(albumCounts.items(),key=lambda x: x[1],reverse=True) # 재생한 수가 많으면 앞으로 정렬
    
    for g in sorted_genres:qqqq
        sorted_g = sorted(albums[g[0]],key=lambda x :x[1],reverse=True)
        print(sorted_g)
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])

    return answer