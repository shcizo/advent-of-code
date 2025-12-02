import numpy as np

def main():
    with open("11-input.txt", "r") as file:
        arr = []
        for line in file.readlines():
            char_array = []
            for char in line.strip():
                char_array.append(char)
            arr.append(char_array)
        matrix = np.array(arr)
        dot_columns = np.all(matrix == ".", axis=0)
        dot_rows = np.all(matrix == ".", axis=1)
        coordinates = np.array(np.nonzero(matrix == '#'))
        distance = []
        for i in range(0, coordinates.shape[1]):
            row = coordinates[0, i]
            col = coordinates[1, i]
            for ii in range(i + 1, coordinates.shape[1]):
                next_row = coordinates[0, ii]
                next_col = coordinates[1, ii]
                empty_rows_passed = get_rows_passed(dot_rows[min(row, next_row):max(row,next_row)])
                empty_cols_passed = get_cols_passed(dot_columns[min(col, next_col):max(next_col, col)])
                d = (abs(next_row  - row) + (abs(next_col - col))) + (empty_cols_passed * 999_999) + (empty_rows_passed * 999_999)
                item = i, ii, d
                if distance.count(item) == 0:
                    distance.append(item)
        print(distance)
        print(len(distance))
        s = 0
        for d in distance:
           s += d[2] 

        print(s)

def get_rows_passed(rows: []):
    passed = 0
    for r in rows:
        if r:
            passed += 1
    return passed

def get_cols_passed(rows: []):
    passed = 0
    for r in rows:
        if r:
            passed += 1
    return passed

if __name__ == "__main__":
    main()
