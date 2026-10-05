import itertools

def solve_cryptarithmetic(equation):
    # Split the equation into parts (e.g., "SEND + MORE == MONEY")
    # We assume the format: WORD1 + WORD2 == WORD3
    try:
        left_side, result_word = equation.split('==')
        words_to_add = [w.strip() for w in left_side.split('+')]
        result_word = result_word.strip()
    except ValueError:
        return "Invalid format. Please use 'WORD1 + WORD2 == RESULT'"

    # Get all unique letters from the equation
    all_words = words_to_add + [result_word]
    unique_letters = sorted(list(set("".join(all_words))))

    if len(unique_letters) > 10:
        return "Too many unique letters! (Max 10 allowed)"

    # Optimization: Identify letters that cannot be zero (the first letter of any word)
    first_letters = set(word[0] for word in all_words if len(word) > 1)

    # Try all permutations of digits 0-9 for the number of unique letters
    digits = range(10)
    for permutation in itertools.permutations(digits, len(unique_letters)):
        # Create a mapping of letter to digit
        mapping = dict(zip(unique_letters, permutation))

        # Check if any leading letter is assigned zero
        if any(mapping[letter] == 0 for letter in first_letters):
            continue

        # Helper function to convert word to number based on mapping
        def word_to_num(word):
            num = 0
            for char in word:
                num = num * 10 + mapping[char]
            return num

        # Calculate the sum of the left side
        sum_left = sum(word_to_num(w) for w in words_to_add)
        target_val = word_to_num(result_word)

        # Check if the equation holds true
        if sum_left == target_val:
            return f"Solution found: {mapping}"

    return "No solution found."

# Example usage:
if __name__ == "__main__":
    # Change this string to test different puzzles
    puzzle = "SEND + MORE == MONEY"
    print(f"Solving: {puzzle}")
    print(solve_cryptarithmetic(puzzle))
