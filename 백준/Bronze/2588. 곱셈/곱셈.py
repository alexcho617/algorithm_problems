#https://www.acmicpc.net/problem/2588
a = int(input())
b = int(input())
b_str = str(b)
for i in range(len(b_str)-1,-1,-1):
    # print(i)
    print(int(b_str[i]) * a)
print(a*b)