#https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

def solve(people: list):
    ans = 0
    people.sort(key= lambda x: x[0])

    threshold = 1e9
    for p in people:
        if threshold > p[1]:
            ans += 1
            threshold = p[1]
   
    return ans

# arr = [[3,6],[7,3],[4,2],[1,4],[5,7],[2,5],[6,1]]
# print(solve(arr))

for _ in range(int(input())):
    temp = []
    for _ in range(int(input())):
        temp.append(list(map(int,input().split())))
    
    print(solve(temp))