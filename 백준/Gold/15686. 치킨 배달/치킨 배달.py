#https://www.acmicpc.net/problem/15686
import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
graph = []
chickens = []
houses = []
distances = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
for r in range(1,n + 1):
    for c in range(1,n + 1):
        if graph[r-1][c-1] == 1:
            houses.append([r,c])
        elif graph[r-1][c-1] == 2:
            chickens.append([r,c])

def calculateDistance(chickens: list, customers: list):
    # print("====CALCULATE====")
    # print(chickens)
    # print(customers)
    # print("=================")
    distance = 0
    min = 99999
    while customers:
        customer = customers.pop()
        for chicken in chickens:
            d  = abs(chicken[0] - customer[0]) + abs(chicken[1] - customer[1])
            if d < min:
                min = d
        distance += min
        min = 99999
    return distance

chickenCombs = list(combinations(chickens,m))
# print(chickenCombs)
temp=[]
for chickenComb in chickenCombs:
    # print("FOR")
    # print("chickenComb",chickenComb)
    temp=houses[:] #deep copy
    distances.append(calculateDistance(chickenComb,temp))
# print(distances)    
print(min(distances))