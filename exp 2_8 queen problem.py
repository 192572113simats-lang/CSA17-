def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nq_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col] (Backtrack)
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nq_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board, n)
    return True

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(" Q " if board[i][j] == 1 else " . ")
        print()

if __name__ == "__main__":
    n = 8
    solve_n_queens(n)
