# Python program to implement Depth First Search (DFS)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

        return visited

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        print("DFS Traversal (Iterative):", end=" ")
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                # Add neighbors in reverse order to maintain left-to-right traversal
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()


# Driver code
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

    print("DFS Traversal (Recursive):", end=" ")
    g.dfs_recursive('A')
    print()

    g.dfs_iterative('A')
