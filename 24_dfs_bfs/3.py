# https://www.acmicpc.net/problem/2667
# 단지번호붙이기


# n = int(input())
# arr = []
# for _ in range(n):
#     line = input()
#     temp = []
#     for l in line:
#         temp.append(int(l))
#     arr.append(temp)
# print(arr)

def isSafe(grid, row, col, visited):
    return(0 <= row < len(grid) and
           0 <= col < len(grid[0]) and
           grid[row][col] == "1" and visited[row][col] == False)


def dfs(row, col, visited, grid):
    valid_row = [-1, 0, 0, 1]
    valid_col = [0, -1, 1, 0]
    visited[row][col] = True
    for neighbour in range(len(valid_row)):
        new_row = row + valid_row[neighbour]
        new_col = col + valid_col[neighbour]
        if(isSafe(grid, new_row, new_col, visited)):
            dfs(new_row, new_col, visited, grid)


def numIslands(grid) -> int:
    visited = [[False for col in range(len(grid[0]))]
               for row in range(len(grid))]
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "1" and visited[row][col] == False):
                dfs(row, col, visited, grid)
                count += 1
    return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

print(numIslands(graph))