# https://www.acmicpc.net/problem/2217
# 로프
n = int(input())
ans = 0
rope = []
# usedRope=[]
for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(n):
    curr = (i + 1) * rope[i]
    if(ans < curr):
        ans = curr
print(ans)
# print(usedRope)