import numpy as np
import math


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
def main():
    with open("10-input.txt", "r") as file:
        arr = []
        for line in file.readlines():
            char_array = []
            for char in line.strip():
                char_array.append(char)
            arr.append(char_array)
        matrix = np.array(arr)
        print(matrix.shape)
        indices = np.nonzero(matrix == "S")
        row_indices, col_indices = indices
        starting_pos = (row_indices[0], col_indices[0])
        current_position: tuple = starting_pos
        last_position: tuple = starting_pos
        steps = 0
        visited = []
        while True:
            visited.append(current_position)
            current = matrix[current_position]
            next_position = find_next(current, current_position, last_position)
            print(f"steps: {steps}: current {current} next {next_position}")
            last_position = current_position
            current_position = next_position
            steps += 1

            if next_position == starting_pos:
                break
        half = steps / 2
        print(math.ceil(half))
        rows, cols = zip(*visited)
        new_matrix = matrix[rows, cols]
        print(new_matrix.shape)


def find_next(pipe: str, position: tuple, last_position: tuple):
    row_index, col_index = position
    last_row_index, last_col_index = last_position
    # print(pipe)
    match pipe:
        case "|":
            if last_row_index > row_index:
                return (row_index - 1, col_index)
            return (row_index + 1, col_index)
        case "-":
            if last_col_index > col_index:
                return (row_index, col_index - 1)
            return (row_index, col_index + 1)
        case "L":
            if last_col_index > col_index:
                return (row_index - 1, col_index)
            return (row_index, col_index + 1)
        case "J":
            if last_col_index < col_index:
                return (row_index - 1, col_index)
            return (row_index, col_index - 1)
        case "7":
            if last_col_index < col_index:
                return (row_index + 1, col_index)
            return (row_index, col_index - 1)
        case "F":
            if last_row_index > row_index:
                return (row_index, col_index + 1)
            return (row_index + 1, col_index)
        case "S":
            return (row_index + 1, col_index)


if __name__ == "__main__":
    main()
