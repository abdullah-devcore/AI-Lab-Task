#BFS
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
queue = []

def bfs(node):
    queue.append(node)

    while queue:
        print(queue, visited)
        temp = queue.pop()
        visited.append(temp)   
        
        for child in graph[temp]:
            queue.append(child)

bfs("A")

print("Visited:", visited)
print("Queue:", queue)