#https://www.acmicpc.net/problem/2592
from collections import Counter

arr = []
for i in range(10):
    arr.append(int(input()))

# arr = [int(input()) for _ in range(10)]  

cnt = Counter(arr).most_common()
print(sum(arr)//10)
print(cnt[0][0])
