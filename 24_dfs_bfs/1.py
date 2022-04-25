#https://www.acmicpc.net/problem/1260
#DFS와 BFS


#DFS uses stack // recursion
def dfs(graph,node):
    visited = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            #for stack, descending order for visiting lower value nodes
            stack += sorted(list(graph[node] - set(visited)), reverse = True)
    return visited

#BFS uses queue
def bfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            #for queue, ascending order for visiting lower value nodes
            queue += sorted(list(graph[node] - set(visited)))
    return visited


#input
n,m,v = map(int,input().split())

#index와 vertex 숫자를 를 맞추기 위해 n+1갯수로 초기화 하며 [0]은 사용하지 않는다.
graph = [set([])for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)



result1 = dfs(graph,v)
print(*result1)

result2 = bfs(graph,v)
print(*result2)
