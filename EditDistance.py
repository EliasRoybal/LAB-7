# This implements the edit distance algorithm
def edit_distance(word_one, word_two, m, n):
    # If first string is empty, characters in second string are inserted into first
    if m == 0:
        return n

        # If second string is empty, all characters in first string are removed
    if n == 0:
        return m

        # Checks to see if last characters match. If so, it ignores and gets count for other strings
    if word_one[m - 1] == word_two[n - 1]:
        return edit_distance(word_one, word_two, m - 1, n - 1)

        # If the last characters don't match, it takes the smallest cost between
        # insert, remove, and replace
    return 1 + min(edit_distance(word_one, word_two, m, n - 1),  # Insert
                   edit_distance(word_one, word_two, m - 1, n),  # Remove
                   edit_distance(word_one, word_two, m - 1, n - 1)  # Replace
                   )
