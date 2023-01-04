# https://www.acmicpc.net/problem/2630
white, blue = 0,0

def divide(graph: list):
    half = len(graph) //2 
    s1,s2,s3,s4 = [],[],[],[]

    for i in range(half):
        s1.append(graph[i][:half])
        s2.append(graph[i][half:])
    for i in range(half, len(graph)):
        s3.append(graph[i][:half])
        s4.append(graph[i][half:])
    return s1,s2,s3,s4
def recursion(graph: list, n: int):
    global white, blue
    if all(0 not in l for l in graph):
        blue += 1
        return
    if all(1 not in l for l in graph):
        white += 1
        return 
    else:
        for section in divide(graph):
            recursion(section, n//2)
    
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
recursion(graph,n)
print(white)
print(blue)