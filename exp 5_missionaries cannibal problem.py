from collections import deque

class State:
    def __init__(self, m_left, c_left, boat, m_right, c_right):
        self.m_left = m_left
        self.c_left = c_left
        self.boat = boat  # 1 for left bank, 0 for right bank
        self.m_right = m_right
        self.c_right = c_right
        self.parent = None

    def is_valid(self):
        if self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
            return False
        if (self.m_left > 0 and self.m_left < self.c_left) or (self.m_right > 0 and self.m_right < self.c_right):
            return False
        return True

    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0

    def __eq__(self, other):
        return (self.m_left == other.m_left and self.c_left == other.c_left and
                self.boat == other.boat and self.m_right == other.m_right and
                self.c_right == other.c_right)

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.boat, self.m_right, self.c_right))

def get_successors(state):
    successors = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for m, c in moves:
        if state.boat == 1:  # Boat is on the left
            new_state = State(state.m_left - m, state.c_left - c, 0, state.m_right + m, state.c_right + c)
        else:  # Boat is on the right
            new_state = State(state.m_left + m, state.c_left + c, 1, state.m_right - m, state.c_right - c)
        
        if new_state.is_valid():
            new_state.parent = state
            successors.append(new_state)
    return successors

def solve():
    initial_state = State(3, 3, 1, 0, 0)
    if initial_state.is_goal():
        return initial_state

    queue = deque([initial_state])
    visited = {initial_state}

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state

        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
    return None

def print_solution(solution):
    path = []
    curr = solution
    while curr:
        path.append(curr)
        curr = curr.parent
    
    path.reverse()
    print(f"{'Left M':<8} {'Left C':<8} {'Boat':<8} {'Right M':<8} {'Right C':<8}")
    for s in path:
        boat_pos = "Left" if s.boat == 1 else "Right"
        print(f"{s.m_left:<8} {s.c_left:<8} {boat_pos:<8} {s.m_right:<8} {s.c_right:<8}")

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Solution Found:")
        print_solution(solution)
    else:
        print("No solution found.")
