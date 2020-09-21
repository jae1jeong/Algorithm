import sys



'''
sys 내장모듈로 input 보다 성능이 좋은 sys.stdin.readline().strip() 사용
strip() 공백 제거 함수
'''
n,m = map(int,sys.stdin.readline().strip().split())

# cash 리스트에 입력을 받는다. 리스트 간단하게 입력 받는법을 드디어 찾았다.
cash = list(reversed([int(sys.stdin.readline()) for _ in range(n)]))

# 카운트 전역변수 설정
count = 0

# for문으로 cash -> coin 만약 m(머니)가 코인보다 크거나 같다면
for coin in cash:
    if m >= coin:
        # 소수점을 제외한 횟수
        cnt = m //coin
        # 카운트에 추가
        count += cnt
        # 머니(m) 을 카운트와 코인의 곱을 계속 빼준다.
        m -= cnt * coin


print(count)
