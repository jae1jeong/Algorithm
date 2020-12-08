l = int(input())
boxes = list(map(int,input().split()))
m = int(input())

# def clean(arr:list):
#     higher_box = max(arr)
#     higher_box_idx = arr.index(higher_box)
#     lower_box = min(arr)
#     lower_box_idx = arr.index(lower_box)
#     arr[higher_box_idx] -= 1
#     arr[lower_box_idx] += 1
#     return arr

# for _ in range(m):
#     boxes = clean(boxes)
# print(max(boxes)-min(boxes))

# 진짜 멍청한 방법이였다. 통과는 했지만 코드 수도 많고 시간 복잡도도 많이 걸린다. index O(N) max,min함수 0(N)

boxes.sort()
for _ in range(m):
    boxes[-1] -= 1
    boxes[0] += 1
    boxes.sort()
print(boxes[-1]-boxes[0])

#아마 O(nlogn)

        