from collections import deque

def bfs(adjlist, start):
    count = 0
    que = deque()
    visited = []
    que.append(start)
    while que:
        curr = que.popleft()
        if curr not in visited:
            visited.append(curr)
            count += 1
        if adjlist[curr]:
            nodes = adjlist[curr]
            for node in nodes:
                if node not in visited:
                    que.append(node)
    return count

def solution(n, wires):
    answer = 999
    #줄을 하나씩 자르면서 하나의 아일랜드를 BFS/DFS 탐색하여 노드를 카운트 한다.
    #카운트 된 노드를 총 송전탑의 갯수인 n에서 빼어 그 차이의 절댓값을 구한다.
    #절댓값을 기록하며 미니멈을 구한다.
    #이것이 가능한 이유는 네트워크는 항상 트리이기 때문에 하나의 전선을 끊었을 경우 아일랜드가 총 2개가 생긴다는것을 보장하기 때문이다.만약 네트워크에 싸이클이 있다면 이 방법은 유효하지 않다.
    
    #구현
    #그래프 매트릭스, 리스트 중? 그래프를 꼭 써야하나?
    #1. 인접 리스트 만든다 index가 해당 노드
    adjlist = [[] for _ in range(n+1)]
    for wire in wires:
        adjlist[wire[0]].append(wire[1])
        adjlist[wire[1]].append(wire[0])
    #2.loop nodes and do bfs counting
    for wire in wires:
        a,b = wire
        #cut wire
        adjlist[a].remove(b)
        adjlist[b].remove(a)
        count = bfs(adjlist,a) #call bfs and receive count
        print(wire,count)
        #restore wire
        adjlist[a].append(b)
        adjlist[b].append(a)
        #3. abs() difference and find minimum
        answer = min(answer,abs(count-(n-count)))
    return answer