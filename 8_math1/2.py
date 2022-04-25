#https://www.acmicpc.net/problem/2292
#벌집

#iteration with increasing i
#increment sum by i*6
#compare with n
#print i - 1 when sum gets larger
n = int(input())
i = 1
sum = 1

while(sum < n):
    sum += (i * 6)
    i += 1
print(i)
