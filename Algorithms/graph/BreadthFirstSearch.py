import queue

"""
implements breadth first search for
"""


def breadth_first_search(graph):
    bfs_queue = queue.Queue()
    visited = set()
    count = 0
    for i in range(len(graph)):
        if i not in visited:
            # start BFS
            bfs_queue.put(i)
            visited.add(i)
            count += 1
            while not bfs_queue.empty():
                row_num = bfs_queue.get()
                visited.add(row_num)
                for j in range(len(graph)):
                    if graph[row_num][j] is 1 and row_num != j and j not in visited:
                        bfs_queue.put(j)
    return count


connected_graph = [[1, 0, 0, 0, 1, 1],
                   [0, 1, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0, 0],
                   [1, 0, 0, 0, 1, 1],
                   [0, 0, 0, 0, 1, 1]]
print(breadth_first_search(connected_graph) == 2)
