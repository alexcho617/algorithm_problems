#https://www.acmicpc.net/problem/10610

num = list(input())
sum = 0
for n in num:
    
    sum += int(n)
if (sum % 3) == 0: # multiple of 3
    if '0' in num: #multiple of 10
        num.sort(reverse = True) #reverse order
        for n in num: print(n, end = '')
        print()
        quit()
print('-1')
