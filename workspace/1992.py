# https://www.acmicpc.net/problem/1992
import sys
input = sys.stdin.readline


def recursion(graph: list, n: int):
    # escape
    # count 0 1
    if all('0' not in l for l in graph):  # if there is no 0 in graph
        return "1"
    if all('1' not in l for l in graph):  # if there is no 1 in graph
        return "0"

    else:
        temp = []
        str = ""
        # divide
        # topleft
        for i in range(n//2):
            temp.append(graph[i][0:n//2])
        str += recursion(temp, n//2)
        temp.clear()
        # topright
        for i in range(n//2):
            temp.append(graph[i][n//2:])
        str += recursion(temp, n//2)
        temp.clear()

        # bottomleft
        for i in range(n//2,n):
            temp.append(graph[i][0:n//2])
        str += recursion(temp, n//2)
        temp.clear()

        # bottomright
        for i in range(n//2,n):
            temp.append(graph[i][n//2:])
        str += recursion(temp, n//2)
        temp.clear()

        return "(" + str + ")"



n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    str = input().strip()
    for s in str:
        graph[i].append(s)

# print(graph)
print(recursion(graph,n))
