import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic (estimated cost from current to end)
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    start_node = Node(None, start)
    end_node = Node(None, end)

    # open_list contains nodes to be evaluated, closed_list contains nodes already evaluated
    open_list = []
    closed_list = set()

    # Add the start node
    heapq.heappush(open_list, start_node)

    # Loop until you find the end
    while open_list:

        # Get the current node (the one with the lowest f score)
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children (neighbors)
        (r, c) = current_node.position
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

        for next_pos in neighbors:

            # Make sure within range
            if (next_pos[0] < 0 or next_pos[0] >= len(maze) or 
                next_pos[1] < 0 or next_pos[1] >= len(maze[0])):
                continue

            # Make sure walkable terrain (0 is walkable, 1 is wall)
            if maze[next_pos[0]][next_pos[1]] != 0:
                continue

            # If already visited
            if next_pos in closed_list:
                continue

            # Create new node
            child = Node(current_node, next_pos)

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # Using Euclidean distance as heuristic
            child.h = ((child.position[0] - end_node.position[0]) ** 2 + 
                       (child.position[1] - end_node.position[1]) ** 2) ** 0.5
            child.f = child.g + child.h

            # Child is already in the open list with a lower g cost
            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    return None


# --- Test the implementation ---
if __name__ == "__main__":
    # 0 = empty space, 1 = wall
    grid = [[0, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]

    start = (0, 0)
    end = (4, 5)

    path = astar(grid, start, end)
    print(f"Path found: {path}")
