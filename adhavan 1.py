import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, parent=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.parent = parent
        self.empty_pos = self.board.index(0)
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i in range(9):
            if self.board[i] != 0:
                target_idx = self.goal.index(self.board[i])
                curr_r, curr_c = divmod(i, 3)
                goal_r, goal_c = divmod(target_idx, 3)
                distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
        return distance

    def get_neighbors(self):
        neighbors = []
        r, c = divmod(self.empty_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = list(self.board)
                neighbor_pos = nr * 3 + nc
                new_board[self.empty_pos], new_board[neighbor_pos] = new_board[neighbor_pos], new_board[self.empty_pos]
                neighbors.append(PuzzleState(tuple(new_board), self.goal, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.priority < other.priority

def solve_8_puzzle(start_board, goal_board):
    start_state = PuzzleState(tuple(start_board), tuple(goal_board))
    open_set = []
    heapq.heappush(open_set, start_state)
    visited = {tuple(start_board)}

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.board == tuple(goal_board):
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]

        for neighbor in current_state.get_neighbors():
            if neighbor.board not in visited:
                visited.add(neighbor.board)
                heapq.heappush(open_set, neighbor)
    return None

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

if __name__ == "__main__":
    # 0 represents the empty space
    initial_state = [1, 2, 3, 
                     4, 0, 6, 
                     7, 5, 8]

    goal_state = [1, 2, 3, 
                  4, 5, 6, 
                  7, 8, 0]

    print("Solving 8-Puzzle...\n")
    solution = solve_8_puzzle(initial_state, goal_state)

    if solution:
        print(f"Solution found in {len(solution) - 1} moves!\n")
        for step in solution:
            print_board(step)
    else:
        print("No solution exists.")
