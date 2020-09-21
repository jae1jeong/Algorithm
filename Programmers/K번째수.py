






def solution(array,commands):
    answer = []
    test = []

    for idx in range(0,len(commands)):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
        test = sorted(array[i - 1:j])
        answer.append(test[k - 1])

    return answer

