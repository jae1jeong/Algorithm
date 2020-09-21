N, M = map(int, input().split())
team_mem, mem_team = {}, {}

for _ in range(N):
    team_name, number = input(), int(input())
    team_mem[team_name] = []
    for i in range(number):
        name = str(input())
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for j in range(M):
    who = input()
    n = int(input())

    if n == 0:

        for member in sorted(team_mem[who]):
            print(member)
    elif n == 1:
        print(mem_team[who])
