def solution(priorities,location):
    
    queue= [(q,idx) for idx,q in enumerate(priorities)]
    cnt = 0
    
    while True:
        if queue[0][0] == max(queue,key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == location:
                break

            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
    return cnt

p = [2, 1, 3, 2]
loc = 2
solution(p,loc)