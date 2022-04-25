#https://www.acmicpc.net/problem/10872
#팩토리얼

#f(n) = n * f(n-1)
def factorial(n):
    #constraint
    assert n >= 0, 'Positive Integer Only'
    #base case
    if n in [0,1]:
        return 1
    #recursion case
    else: 
        return n * factorial(n-1)

n = int(input())
print(factorial(n))