def search(graph, vertex, visited, parent) -> bool:
    """dfs returning boolean if there's a cycle for the current start node"""
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if search(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True

    return False


def has_cycle(graph):
    visited = {v: False for v in graph.keys()}

    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, None):
                return True
    return False


# graph = {1: [2, 3], 2: [4], 3: [], 4: []}
graph = {
    "JFK": ["SFO", "LAX"],
    "SFO": ["ORL"],
    "ORL": ["JFK", "LAX", "DFW"],
    "LAX": ["DFW"],
}
print(has_cycle(graph))
