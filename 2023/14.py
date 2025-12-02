import numpy as np

def hash_(array):
    return tuple(array.ravel())

def score(matrix):
    total_count = 0
    for i in range(matrix.shape[0]):
        row = matrix[i, :]
        count_O = np.count_nonzero(row == 'O') * (matrix.shape[0] - i)
        total_count += count_O
        #print(f"Row {i + 1} has {count_O} 'O's")
    print(f"Total count: {total_count}")
    return total_count

# Read the file
file_path = '14-input.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Split each line into individual characters
lines = [list(line.strip()) for line in lines]

# Build a NumPy matrix of all the lines
matrix = np.array(lines)
seen_matrices = []
seen = {}
scores = {}
maxval = 1_000_000_000
# Loop through each column in the matrix
for cycle in range(maxval):
    print(f"Cycle {cycle + 1}")
    h = hash_(matrix)
    if h in seen:
        print(matrix)
        scores[cycle] = score(matrix)
        print(f"Found cycle at {cycle + 1}")
        break
    seen[h] = cycle
    s = score(matrix)
    scores[cycle] = s
    for s in range(4):
        for i in range(matrix.shape[1]):
            column = matrix[:, i]
            c_length = column.shape[0]
            if np.any(column == 'O'):
                for c in range(c_length):
                    if column[c] == '.':
                        for r in range(c, c_length):
                            if column[r] == '#':
                                break
                            if column[r] == 'O':
                                column[c] = 'O'
                                column[r] = '.'
                                break

        matrix = np.rot90(matrix, -1)
    
print(scores)
cycle_length = cycle - seen[h]
index = seen[h] + (maxval - seen[h]) % cycle_length

print(f"Total count: {scores[index]}")