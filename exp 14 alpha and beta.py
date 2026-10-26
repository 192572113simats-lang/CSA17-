def minimax(depth, node_index, is_maximizing, values, alpha, beta):
    # Base case: leaf node reached
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best = float('-inf')
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best

# Driver code
if __name__ == "__main__":
    # Example leaf nodes of a game tree
    # This represents a tree with a depth of 3 (8 leaves)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    print("The optimal value is:", minimax(0, 0, True, values, float('-inf'), float('inf')))
