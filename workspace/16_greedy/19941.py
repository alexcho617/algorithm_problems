#https://www.acmicpc.net/problem/19941
n,k = map(int,input().split())
line = list(input())
ans = 0
#iterate line
for i in range(len(line)):
    #people come up
    if line[i] == 'P':
        #if there is burger on left eat it
        #i-k ~ i
        for j in range(i-k,i+k+1):
            if j >= 0 and j < n:
                if line[j] == 'H':
                    ans +=1
                    line[j] = 'N'
                    break
        #otherwise cannot eat
print(ans)