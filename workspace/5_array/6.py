n = int(input())

for i in range(n):
    test = input()
    totalScore = 0
    conseq = 0
    for t in test:
        if t == "O":
            conseq += 1
            totalScore += conseq
        else:
            conseq = 0
    print(totalScore)