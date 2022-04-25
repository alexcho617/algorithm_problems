#https://www.acmicpc.net/problem/10870
#피보나치 수 5
#Fn = F(n-1) + F(n-2 (n ≥ 2)

def fibonacci(n):
    #constraint
    assert n >= 0, 'only positive interger'
    #base case
    if n in [0,1]: 
        return n
    #recursion case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))