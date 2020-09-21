from itertools import *


def solution(answers):
    answers = [1,2,3,4,5]
    winner = []
    sp1 = [1,2,3,4,5]
    sp2 = [2,1,2,3,2,4,2,5]
    sp3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0 for _ in range(3)] # [0,0,0]

    for s1,s2,s3,answer in zip(cycle(sp1),cycle(sp2),cycle(sp3),answers): # [sp1[0],sp2[0],sp3[0].score[0]
        if s1 == answer:
            score[0] +=1
        if s2 == answer:
            score[1] +=1
        if s3 == answer:
            score[2] +=1

    for i,s in enumerate(score): # 제일 큰 수였던 리스트 인덱스를 append
        if s == max(score):
            winner.append(i+1)

    return winner