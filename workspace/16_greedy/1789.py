#https://www.acmicpc.net/problem/1789
s = int(input())
sum = 0
increment = 1
ans = 0

while True:
    if (sum + increment) <= s:    
        sum += increment
        increment += 1
        ans += 1
    else:
        break
print(ans)
