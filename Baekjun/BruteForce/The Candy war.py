def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1

    return len(set(candy)) == 1  # 중복되면 set는 하나가 되기 때문에 원소들이 다 똑같다면 1이됨


def teacher(N, candy):
    tmp_list = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:  # 홀수 경우 1을 더해주고
            candy[idx] += 1

        candy[idx] //= 2  # 절반으로 나누고
        # 절반으로 나눈 값을 tmp_list를 저장하면서 오른쪽 아이에게 줄 배열을 저장
        tmp_list[(idx+1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_list[idx]  # 오른쪽 아이가 캔디를 나눠준다

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for i in range(int(input())):
    process()
