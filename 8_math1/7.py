#https://www.acmicpc.net/problem/2839
#설탕 배달





#dp
import sys

read = sys.stdin.readline
N = int(read())

arr = [5001] * (N+5)
arr[3] = arr[5] = 1

for i in range(6, N+1):
    arr[i] = min(arr[i-3], arr[i-5]) + 1

print(arr[N] if arr[N] < 5001 else -1)

#brute force
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)