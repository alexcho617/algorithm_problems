# https://www.acmicpc.net/problem/11729
# 
# Recursive Python function to solve the tower of hanoi
record = []
def TowerOfHanoi(n , source, destination, auxiliary):
    global record
    if n==1:
        record.append([source, destination])
    else:
        TowerOfHanoi(n-1,source, auxiliary ,destination)
        record.append([source,destination])
        TowerOfHanoi(n-1,auxiliary, destination, source)



n = int(input())
TowerOfHanoi(n,1,3,2)
print(len(record))
for r in record:
    print(*r)
