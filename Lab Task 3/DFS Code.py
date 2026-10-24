#DFS
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

visited = []
stack = []

def dfs(node):
    stack.append(node)

    while stack:
        print(stack, visited)
        temp = stack.pop()
        visited.append(temp)   
        
        for child in graph[temp]:
            stack.append(child)

dfs("A")

print("Visited:", visited)
print("Stack:", stack)

