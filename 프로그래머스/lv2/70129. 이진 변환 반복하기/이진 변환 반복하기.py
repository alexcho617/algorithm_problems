def solution(x):
    zeros = 0
    functionCount = 0
    
    def binaryConversion(x: str):
        #remove 0, get number of 0s removed
        numberOfZeros = x.count("0")

        #get length of x = c
        c = len(x.replace("0", ""))

        #turn length to binary
        x = bin(c)
        x = x[2:]
        return numberOfZeros, x
    
    while True:
        if x == "1": break
        zeroCount, x = binaryConversion(x)
        zeros += zeroCount
        functionCount += 1
        print(zeroCount, x, functionCount)
    
    return [functionCount, zeros]