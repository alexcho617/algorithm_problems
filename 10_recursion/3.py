#https://www.acmicpc.net/problem/2447
#별 찍기 - 10

def printStar(n):
    if(n == 1): 
        print('n is 1')
    else:
        print('***\n* *\n***'* n)
        return printStar(int(n/3))

printStar(int(input()))