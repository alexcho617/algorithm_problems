#https://www.acmicpc.net/problem/2810
n = int(input())
seats = input()
ans = 0
temp = ''
lcount= 0
for s in seats:
    if s == 'S':
        ans += 1
    elif s == 'L':
        temp += s
        if temp == 'LL':
            temp = ''
            ans += 1
            if lcount == 0:
                ans += 1
            lcount += 1

print(ans)