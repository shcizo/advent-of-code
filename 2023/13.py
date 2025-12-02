import numpy as np


filename = "13-input.txt"

def main():
    with open(filename, "r") as file:
        arr = []
        nr_reflections = 0
        pattern = 0
        for i, line in enumerate(file):
            if line == "\n":
                if arr:
                    pattern += 1
                    print(f"Pattern {pattern}")
                    matrix = np.array(arr)
                    r = get_reflections(matrix)
                    print(f"Found {r} reflections")
                    if r <= 0:
                        print("Rotating 90 degrees")
                        r = get_reflections(np.rot90(matrix)) * 100
                        print(f"Found {r} reflections")
                    nr_reflections += r
                    arr = []
                    continue
            char_array = []
            for char in line.strip():
                char_array.append(char)
            arr.append(char_array)

        print(nr_reflections)

def get_reflections(matrix: []):
    f = {}
    for i in range(0, matrix.shape[0] - 1):
        for ii in range(i, matrix.shape[1] + 1, 2):
            part_matrix = matrix[:, i:ii]         
            first, second = fold_matrix(part_matrix)
            if first.size > 0 and second.size > 0 and np.all(first == second):
                #if np.all(np.any(part_matrix == '#', axis=1)):
                print(f"Found reflection at {i}, {ii}")
                f[part_matrix.size] = ((ii - i) // 2) + i

    if not f:
        return 0
    # Sort the dictionary in descending order of keys
    sorted_f = dict(sorted(f.items(), key=lambda item: item[0], reverse=True))
     # Return the value of the first item in the sorted dictionary
    return sorted_f.popitem()[1]

def fold_matrix(matrix: []):
    if matrix.shape[1] % 2 != 0:
        return np.empty(0), np.empty(0)
    half = matrix.shape[1] // 2
    first_half = matrix[:, :half]
    second_half = np.flip(matrix[:, half:], axis=1)
    # if len(matrix) % 2 != 0:
    #     second_half = np.vstack([second_half, np.zeros_like(first_half[0])])
    return first_half, second_half

if __name__ == "__main__":
    main()
