n = int(input())
score = list(map(int,input().split()))
max = max(score)
score = [x/max*100 for x in score]
print(sum(score)/n)