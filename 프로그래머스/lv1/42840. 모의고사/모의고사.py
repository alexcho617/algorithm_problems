def solution(answers):
    answer = []
    count = [0,0,0]
    personOne = [1,2,3,4,5]
    personTwo = [2,1,2,3,2,4,2,5]
    personThree = [3,3,1,1,2,2,4,4,5,5]
    lengthOne, lengthTwo, lengthThree = len(personOne), len(personTwo), len(personThree)
    # print(lengthOne,lengthTwo,lengthThree)
    j,k,l = 0,0,0 #loop variables
    for index in range(len(answers)):
        #answer check
        currentAnswer = answers[index]
       
        if currentAnswer == personOne[j]:
            count[0] += 1
        if currentAnswer == personTwo[k]:
            count[1] += 1
        if currentAnswer == personThree[l]:
            count[2] += 1
        
        j += 1
        k += 1
        l += 1
        
        if j == lengthOne:
            j = 0
        if k == lengthTwo:
            k = 0
        if l == lengthThree:
            l = 0
        
    # print(count)
    #출력
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)
    return answer