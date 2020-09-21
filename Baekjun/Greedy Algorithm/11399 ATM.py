# 개수 입력
n = int(input())

# 인출하는 사람 인원 입력
P = list(map(int,input().split()))
# 걸리는 시간의 합을 더하기 위해 리스트 a선언 그리고 0 초기화
a = [0 for i in range(n)]
# 리스트의 원소 걸리는 시간 리스트를 계산하기 위해 result 변수 선언
result = 0

# 개수가 1이라면 바로 반환
if n ==1:
    print(P[0])
else:
    # 가장 작은 숫자들이 먼저 나오면 걸리는 시간이 작아지니까 정렬
    P.sort()
    # 0부터 n까지 반복하면서 a에 걸리는 시간을 담는다.
    for i in range(0,n):
        result += P[i]
        a[i] = result
    # 리스트 a에 모두 더한 후 리스트 원소를 다 더해주는 sum으로 출력
    print(sum(a))

