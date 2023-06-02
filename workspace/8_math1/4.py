#https://www.acmicpc.net/problem/2869
#달팽이는 올라가고 싶다

# import math
a,b,v = map(int,(input().split()))

# d= math.ceil((v-a)/(a-b)) + 1
d = (v-b) / (a-b)
if(d == int(d)):
    d = int(d)
else: d = int(d)+1

print(d)

