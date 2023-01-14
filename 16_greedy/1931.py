#https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline
n = int(input())
meetingTable = []
for _ in range(n):
    meetingTable.append(list(map(int,input().split())))
meetingTable.sort(key = lambda x: (x[1], x[0]))

ans = 1
start,finish = meetingTable[0][0],meetingTable[0][1]
#pick meetings with smallest finish time
for meeting in meetingTable[1:]:
    #start of current must be larger than finish of previous
    if meeting[0] >= finish:
        start = meeting[0]
        finish = meeting[1]
        ans += 1

print(ans)