def solution(brown, yellow):
    num = brown + yellow
    pairs = []
    yellowPairs = []
    for i in range(3,int(num ** 0.5 + 1)):
        if num % i == 0:
            pairs.append([i,int(num/i)])
    
    print(pairs)
    for pair in pairs:
        x,y = pair[0] - 2, pair[1] - 2
        if x*y == yellow:
            return [pair[1],pair[0]]
        