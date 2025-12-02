import numpy as np
from base import AoCBase
from typing import List


class Day8(AoCBase):
    def __init__(self):
        super().__init__(8)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0
        np.set_printoptions(threshold=np.inf)
        data = np.array([list(row) for row in self.data])
        u = np.unique_values(data)
        dict = {}
        antennas = {}
        for val in u:
            if val == ".":
                continue
            indices = np.argwhere(data == val)
            for idx in indices:
                row, col = idx
                antennas[(row, col)] = val
                for i in range(0, len(indices)):
                    idx_2 = indices[i]
                    row, col = idx - idx_2  # -1 ,3
                    row_2, col_2 = idx_2 - idx  # 1, -3
                    if row == 0 and col == 0:
                        continue
                    a_r, a_c = idx + np.array([row, col])
                    a2_r, a2_c = idx_2 + np.array([row_2, col_2])
                    dict[(a_r, a_c)] = (a_r, a_c)
                    dict[(a2_r, a2_c)] = (a2_r, a2_c)

        shape = data.shape

        for k in dict:
            if k[0] >= 0 and k[1] >= 0 and k[0] < shape[0] and k[1] < shape[1]:
                data[k[0], k[1]] = "#"
                result += 1

        s = np.array2string(data, 250)
        v = replace_chars(s)
        with open('output.txt', 'w') as f:
            f.write(v)
 
        return result

    def part2(self) -> int:
        result = 0
        np.set_printoptions(threshold=np.inf)
        data = np.array([list(row) for row in self.data])
        u = np.unique_values(data)
        dict = {}
        antennas = {}
        shape = data.shape
        for val in u:
            if val == ".":
                continue
            indices = np.argwhere(data == val)
            for idx in indices:
                row, col = idx
                antennas[(row, col)] = val
                for i in range(0, len(indices)):
                    idx_2 = indices[i]
                    row, col = idx - idx_2  # -1 ,3
                    row_2, col_2 = idx_2 - idx  # 1, -3
                    if row == 0 and col == 0:
                        continue

                    a_r, a_c = (0, 0)
                    a2_r, a2_c = (0, 0)
                    curr_idx = idx
                    curr_idx_2 = idx_2
                    while True:
                        a_r, a_c = curr_idx + np.array([row, col])
                        a2_r, a2_c = curr_idx_2 + np.array([row_2, col_2])
                        dict[(a_r, a_c)] = (a_r, a_c)
                        dict[(a2_r, a2_c)] = (a2_r, a2_c)
                        print(a_r, a_c)
                        print(a2_r, a2_c)
                        curr_idx = np.array([a_r, a_c])
                        curr_idx_2 = np.array([a2_r, a2_c])

                        idx_ob = is_index_in_bounds(data, a_r, a_c)
                        idx_ob_2 = is_index_in_bounds(data, a2_r, a2_c)
                        if (not idx_ob) and (not (idx_ob_2)):
                            break
                        
        for k in dict:
            if k in antennas:
                continue
            if k[0] >= 0 and k[1] >= 0 and k[0] < shape[0] and k[1] < shape[1]:
                data[k[0], k[1]] = "#"
                result += 1

        result += len(antennas)
        s = np.array2string(data, 250)
        v = replace_chars(s)
        with open('output.txt', 'w') as f:
            f.write(v)
 
        return result
    
# Function to check if an index is within bounds
def is_index_in_bounds(array, row, col):
    num_rows, num_cols = array.shape
    return 0 <= row < num_rows and 0 <= col < num_cols

def replace_chars(input_string):
    # Replace single quote
    updated_string = input_string.replace("'", "")
    # Replace open square bracket
    updated_string = updated_string.replace("[", "")
    # Replace close square bracket
    updated_string = updated_string.replace("]", "")
     # Remove spaces
    updated_string = updated_string.replace(" ", "")
    

    return updated_string


if __name__ == "__main__":
    solution = Day8()
    solution.solve()
