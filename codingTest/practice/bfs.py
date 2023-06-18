from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += set(graph[n]) - set(visited)
    return visited
  
graph_list = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}
root_node = 1
print(BFS_with_adj_list(graph_list, root_node))