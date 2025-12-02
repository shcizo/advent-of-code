
import numpy as np

# Your input data as a list of strings
data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

# Convert each row into a list of characters, then stack them into an array
array = np.array([list(row) for row in data])

# Display the array
print(array)