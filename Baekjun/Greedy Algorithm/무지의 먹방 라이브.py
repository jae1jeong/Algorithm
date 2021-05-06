import sys
sys.stdin = open('input.txt','r')

# 시간 초과
# def solution(food_times, k):
#     answer = 0
#     time = 0
#     flag = True
#     while flag:     
#         for i in range(len(food_times)):
#             if food_times[i] == 0:
#                 continue
#             if time == k:
#                 answer = i + 1
#                 flag = False
#                 break
#             food_times[i] -= 1
#             time += 1
#     return answer




class Food:
    
    def __init__(self,time,idx):
        self.time = time
        self.idx = idx


    def __str__(self):
        return f'{self.time},{self.idx}'



food_times = list(map(int,input().split()))
k = int(input())



def solution(food_times, k):

    ans = 0
    lst = []
    for i in range(len(food_times)):
        lst.append(Food(food_times[i],i))
    
    
    lst = sorted(lst,key=lambda x: x.time)
    
    for i in range(len(lst)):
        print(lst[i])
    return ans

solution(food_times,k)