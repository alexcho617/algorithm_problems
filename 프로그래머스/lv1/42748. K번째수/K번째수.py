def solution(array, commands):
    answer = []
    for command in commands:
        # print(command)
        i,j,k = command
        temp = array[i-1:j]
        # print("Splice:",temp)
        temp.sort()
        # print("kth item",temp[k-1])
        answer.append(temp[k-1])
    return answer