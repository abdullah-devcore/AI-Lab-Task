graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": []
}


def dls(node, goal, limit):
    stack = [(node, 0, [node])]
    limit_reached = False

    while stack:
        temp, depth, path = stack.pop()
        if temp == goal:
            return "Goal Found", path
        if depth == limit:
            if graph[temp]:
                limit_reached = True
            continue
        for child in graph[temp]:
            if child not in path:
                stack.append((child, depth + 1, path + [child]))
    if limit_reached:
        return "Limite Reached", None
    return "Failure", None

for limit in range(4):
    status, path = dls("A", "G", limit)
    print(f"Limit: {limit}\nStatus: {status}\nPath: {path}\nLimits attempted: {[limit]}")
