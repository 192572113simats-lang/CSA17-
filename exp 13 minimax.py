import math

def minimax(depth, nodeIndex, isMaximizing, values, targetDepth):
    """
    Implementation of the Minimax algorithm.
    
    :param depth: Current depth in the game tree
    :param nodeIndex: Index of the current node in the values list
    :param isMaximizing: Boolean, True if it is the Maximizer's turn
    :param values: List containing the leaf nodes (terminal values)
    :param targetDepth: The depth at which the leaf nodes are located
    :return: The optimal value for the current player
    """
    
    # Base case: If we have reached the leaf nodes
    if depth == targetDepth:
        return values[nodeIndex]

    if isMaximizing:
        # Maximizer wants the highest possible value
        return max(minimax(depth + 1, nodeIndex * 2, False, values, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, False, values, targetDepth))
    else:
        # Minimizer wants the lowest possible value
        return min(minimax(depth + 1, nodeIndex * 2, True, values, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, True, values, targetDepth))

def solve():
    # Example: A game tree with 8 leaf nodes (depth of 3)
    # These represent the final scores of different game paths
    leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]
    
    # Calculate target depth based on number of leaf nodes (log2 of leaf count)
    tree_depth = int(math.log2(len(leaf_values)))

    print("Leaf nodes in the game tree:", leaf_values)
    
    # Start the minimax process from depth 0
    optimal_value = minimax(0, 0, True, leaf_values, tree_depth)
    
    print(f"The optimal value determined by Minimax is: {optimal_value}")

if __name__ == "__main__":
    solve()
