from collections import deque

visited = []

def bfs(graph, i, j):
    global visited
    root = [i, j]
    queue = deque()
    queue.append(root)
    size = 0

    while queue:
        n = queue.popleft()
        ni = n[0]
        nj = n[1]
        if n not in visited:
            visited.append([ni, nj])
            size += 1

            if not graph[(ni + 1)][nj] == 0:
                queue += [(ni + 1), nj]
            if not graph[(ni - 1)][nj] == 0:
                queue += [(ni - 1), nj]
            if not graph[ni][(nj + 1)] == 0:
                queue += [ni, (nj + 1)]

    return size

def solution(width, height, graph):
    global visited
    max_size = 0
    count = 0

    for i in range(0, width):
        for j in range(0, height):
            if graph[i][j] == 1:
                size = bfs(graph, i, j)
                count += 1
                if size > max_size:
                    max_size = size

    return [count, max_size]

graph_list = [
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
width = 5
height = 6

print(solution(width, height, graph_list))