n = int(input())
for i in range(n):
    studentCount = 0
    average = 0
    above = 0
    data = list(map(int,input().split()))
    average = (sum(data)- data[0])/(data[0])
    studentCount = data[0]
    
    for i in range(1,studentCount+1): #+1 for last data slot access
        if data[i] > average:
            above += 1
    answer = float(above / studentCount)
    print('{:.3%}'.format(answer))