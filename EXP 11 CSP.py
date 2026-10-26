class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables  # List of regions (e.g., ['WA', 'NT', 'SA', ...])
        self.domains = domains      # Dictionary mapping region to list of colors
        self.neighbors = neighbors  # Dictionary mapping region to its adjacent regions

    def is_consistent(self, variable, color, assignment):
        """Check if assigning 'color' to 'variable' violates any constraints."""
        for neighbor in self.neighbors.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, assignment):
        """The core backtracking algorithm to find a valid coloring."""
        # If all variables are assigned, we are done!
        if len(assignment) == len(self.variables):
            return assignment

        # Pick an unassigned variable
        unassigned = [v for v in self.variables if v not in assignment]
        variable = unassigned[0]

        # Try each color in the domain of the chosen variable
        for color in self.domains[variable]:
            if self.is_consistent(variable, color, assignment):
                assignment[variable] = color

                # Recursively attempt to color the rest of the map
                result = self.backtrack(assignment)
                if result is not None:
                    return result

                # If it didn't work, backtrack (remove the assignment)
                del assignment[variable]

        return None

def solve_map_coloring():
    # Define the regions (Variables)
    regions = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

    # Define the available colors (Domains)
    colors = ['Red', 'Green', 'Blue']
    domains = {region: colors for region in regions}

    # Define the adjacency list (Constraints/Neighbors)
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []  # Tasmania is an island, no neighbors
    }

    csp = MapColoringCSP(regions, domains, neighbors)
    solution = csp.backtrack({})

    if solution:
        print("Success! Here is the coloring assignment:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_map_coloring()
