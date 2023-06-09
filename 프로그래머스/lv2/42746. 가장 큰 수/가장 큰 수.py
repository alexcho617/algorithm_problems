def solution(numbers):
    numberList = list(map(str,numbers))
    numberList.sort(key = lambda x : x*3, reverse = True)
    # print(numberList)
    answer = "".join(numberList)
    return str(int(answer))