import itertools

def travelling_salesman_problem(graph, start=0):
    n = len(graph)
    all_nodes = range(n)
    
    # dp[(subset, last_node)] = minimum cost to visit all nodes in subset, ending at last_node
    dp = {}
    
    # Base case: starting at 'start', having visited only 'start'
    dp[(1 << start, start)] = 0
    
    # Iterate over all subsets of nodes
    for subset_size in range(2, n + 1):
        for subset in itertools.combinations(all_nodes, subset_size):
            if start not in subset:
                continue
            bits = 0
            for node in subset:
                bits |= (1 << node)
            
            for last in subset:
                if last == start:
                    continue
                prev_bits = bits & ~(1 << last)
                
                min_cost = float('inf')
                for prev_node in subset:
                    if prev_node == last:
                        continue
                    if (prev_bits, prev_node) in dp:
                        cost = dp[(prev_bits, prev_node)] + graph[prev_node][last]
                        min_cost = min(min_cost, cost)
                
                if min_cost != float('inf'):
                    dp[(bits, last)] = min_cost
    
    # Find the minimum cost to complete the tour (return to start)
    bits = (1 << n) - 1
    min_tour_cost = float('inf')
    for last in all_nodes:
        if last == start:
            continue
        if (bits, last) in dp:
            cost = dp[(bits, last)] + graph[last][start]
            min_tour_cost = min(min_tour_cost, cost)
    
    return min_tour_cost


def print_graph(graph):
    print("Distance Matrix:")
    for row in graph:
        print(row)
    print()


# Example usage
if __name__ == "__main__":
    # Distance matrix (symmetric graph)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    print_graph(graph)
    
    n = len(graph)
    print(f"Number of cities: {n}")
    
    min_cost = travelling_salesman_problem(graph, start=0)
    print(f"\nMinimum cost of Travelling Salesman Tour: {min_cost}")
