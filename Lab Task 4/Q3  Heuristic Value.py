graph = {
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("E", 3), ("D", 2)],
    "C": [("A", 5), ("D", 2)],
    "D": [("B", 2), ("C", 2), ("E", 4)],
    "E": [("B", 3), ("D", 4), ("F", 6)],
    "F": [("E", 6)]
}
# Only C heuristic value is changed
h = {"A": 0,"B": 3,"C": 15,"D": 4,"E": 5,"F": 0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = []

    while len(open_list) > 0:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if g > best[node]:
            continue
        print(node, g, h[node] , f)

        if node == goal:
            print(f"Final Path: {path} , Total Cost: {g} , Expansion Order: {expanded} , Expanded Nodes: {len(expanded)}")
            return
        expanded.append(node)

        for next_node, cost in graph[node]:
            new_g = g + cost

            if next_node not in best or new_g < best[next_node]:
                best[next_node] = new_g
                open_list.append(
                    (new_g + h[next_node], new_g,
                     next_node, path + [next_node])
                )
    print("Goal not found.")

print("Node , g , h , f")
astar("A", "F")
