#https://www.acmicpc.net/problem/16953
a,b = input().split()
a = int(a)
ans = 1
while True:
    if a == int(b):
        break
    elif int(b) >= 11 and b[-1] == '1':
        b = b[:-1]
        ans += 1
    elif b[-1] in ['0','2','4','6','8']:
        b = str(int(b)//2)
        ans += 1
    else:
        print(-1)
        quit()
print(ans)