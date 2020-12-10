import sys
import os

cur_path = os.getcwd()
sys.stdin = open(cur_path+"\\jmbook\\input.txt","r")

c = int(input())

def get_lower_bound(low,high):

    while low < high:
        mid = (low+high)// 2
        if korean[mid] >= russian[best]:
            high = mid
        else:
            low = mid + 1
    return high


for _ in range(c):
    n = int(input())
    russian = list(map(int,input().split()))
    korean = list(map(int,input().split()))
    russian.sort()
    korean.sort()
    best = -1
    worst = 0
    win_cnt = 0

    while russian:
        if russian[best] > korean[best]:
            korean.pop(0)
        else:
            least_rating_kor = get_lower_bound(0,len(korean)-1)
            korean.pop(least_rating_kor)
            win_cnt += 1
        russian.pop()
    print(win_cnt)

