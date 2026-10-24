graph = {
    "A": {"B": 4, "C": 5},
    "B": {"A": 4, "D": 2, "E": 3},
    "C": {"A": 5, "D": 2},
    "D": {"B": 2, "C": 2, "E": 4},
    "E": {"B": 3, "D": 4, "F": 6},
    "F": {"E": 6},
}

h = {"A": 0, "B": 3, "C": 2, "D": 4, "E": 5, "F": 0}
def find_path(start, goal, astar=False):
    open_list = [(0, start, 0, [start])]
    best = {start: 0}
    visited = []

    while open_list:
        item = min(open_list)
        open_list.remove(item)
        f, node, g, path = item

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            print("Visited:", visited)
            print("Path:", path)
            print("Cost:", g)
            return

        for next, w in graph[node].items():
            new_g = g + w

            if next not in best or new_g < best[next]:
                best[next] = new_g
                f_score = new_g + h[next] if astar else new_g
                open_list.append((f_score, next, new_g, path + [next]))
    print("path not found")

#A*
find_path("A", "F", astar=True)

#UCS
find_path("A", "F")