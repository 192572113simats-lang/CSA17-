from collections import deque

def water_jug_problem(jug1_cap, jug2_cap, target):
    # Queue for BFS: (amount_in_jug1, amount_in_jug2, path_taken)
    queue = deque([(0, 0, [])])
    # To keep track of visited states to prevent infinite loops
    visited = set([(0, 0)])

    while queue:
        curr_j1, curr_j2, path = queue.popleft()

        # Check if we reached the target in either jug
        if curr_j1 == target or curr_j2 == target:
            path.append((curr_j1, curr_j2))
            return path

        # List of all possible next moves
        moves = [
            (jug1_cap, curr_j2), # Fill Jug 1
            (curr_j1, jug2_cap), # Fill Jug 2
            (0, curr_j2),        # Empty Jug 1
            (curr_j1, 0),        # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (curr_j1 - min(curr_j1, jug2_cap - curr_j2), curr_j2 + min(curr_j1, jug2_cap - curr_j2)),
            # Pour Jug 2 -> Jug 1
            (curr_j1 + min(curr_j2, jug1_cap - curr_j1), curr_j2 - min(curr_j2, jug1_cap - curr_j1))
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                new_path = path + [(curr_j1, curr_j2)]
                queue.append((move[0], move[1], new_path))

    return None

# --- Execution ---
j1_capacity = 4
j2_capacity = 3
goal = 2

print(f"Solving for Jug1: {j1_capacity}L, Jug2: {j2_capacity}L, Target: {goal}L")
solution = water_jug_problem(j1_capacity, j2_capacity, goal)

if solution:
    print("Steps to reach the goal:")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
else:
    print("No solution possible.")
