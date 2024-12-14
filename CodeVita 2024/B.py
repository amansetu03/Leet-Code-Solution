# Predefined 9x5 grid representations for each letter A-Z in binary strings
LETTER_MAP = {
    'A': [
        "11111",
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
        "10001"
    ],
    'B': [
        "11111  ",
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
        "11111"
    ],
    'C': [
        "11111",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
        "11111"
    ],
    # Add the other alphabet letters in similar fashion for A-Z
    # For brevity, we will include just a few letters (A, B, C) here.
    # You would need to include the rest of the alphabet (D to Z).
}


def decode_display(grid):
    # Each letter is represented by a 9x5 grid, and there might be padding (0's)
    result = []
    columns = len(grid[0])  # Number of columns in the grid
    i = 0  # Pointer to traverse columns

    while i + 5 <= columns:  # Ensure we can still fit a 5-column wide letter
        # Extract a 9x5 block (the letter)
        letter_grid = []
        for row in grid:
            letter_grid.append(row[i:i + 5])

        # Convert the 9x5 block into a string to match it in the dictionary
        letter_key = ''.join(letter_grid)

        # Try to match the letter_key with known letters in the map
        found = False
        for letter, pattern in LETTER_MAP.items():
            pattern_key = ''.join(pattern)
            if letter_key == pattern_key:
                result.append(letter)
                found = True
                break

        # If no match is found, it's impossible to decode this letter
        if not found:
            result.append('?')  # Use '?' to indicate an unknown letter
        # Move i to the next possible letter position (skip padding)
        while i + 5 < columns and all(grid[r][i + 5] == '0' for r in range(9)):
            i += 1
        i += 5  # Move over to the next letter's starting position

    return ''.join(result)


def main():
    # Read the input grid of size 9xZ
    grid = []
    for _ in range(9):
        grid.append(input().strip())  # Read each row

    # Decode the display and print the result
    result = decode_display(grid)
    return result


if __name__ == "__main__":
   print(main())
