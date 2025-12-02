import numpy as np
from base import AoCBase
from typing import List


class Day9(AoCBase):
    def __init__(self):
        super().__init__(9)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip()

    def part1(self) -> int:
        result = 0
        n = list(self.data)
        numbers = np.array(n).astype(int)
        d = []
        id = 0
        for i in range(0, len(numbers)):
            for j in range(0, numbers[i]):
                if i % 2 == 0:
                    d.append(id)
                else:
                    d.append(None)
            if i % 2 == 0:
                id += 1
        
        array = np.array(d)
        none_pos = np.argwhere(array == None)
        pos = np.argwhere(array != None)
        for i in range(0, len(none_pos)):
            if none_pos[i][0] > pos[len(pos) - 1 - i][0]:
                break
            # print("swap", none_pos[i], pos[len(pos) - 1 - i])
            array[[none_pos[i][0], pos[len(pos) - 1 - i][0]]] = array[[pos[len(pos) - 1 - i][0], none_pos[i][0]]]
            # print(array)

        none_pos = np.argwhere(array == None)
        for i in range(0, none_pos[0][0]):
            result += array[i] * i

        return result

    def part2(self) -> int:
        result = 0
        np.set_printoptions(threshold=np.inf, linewidth=np.inf)
        n = list(self.data)
        numbers = np.zeros(len(n), dtype=np.uint8)
        d = [numbers, n]
        d = np.array(d)
        id = 0
        for i in range(0, len(numbers)):
            if i % 2 == 0:
                d[0, i] = id
                id += 1
            else:
                d[0, i] = '.'

        for i in range(d.shape[1] - 1, 0, -1):
            if i % 100 == 0:
                print(i)
            size = d[1, i]
            val = d[0, i]
            if val == '.':
                continue
            positions = np.argwhere(d[0] == '.')
            for pos in positions:
                if pos >= i:
                    continue
                dot_size = d[1, pos][0]
                if dot_size >= size:
                    d = np.insert(d, pos, [[val], [size]], axis=1)
                    new_dot_size = int(dot_size) - int(size)
                    d[1, pos + 1] = new_dot_size
                    d[0, i +1] = '.'
                    break
    
        print(d)
        
        idx = 0
        pos = 0
        while d.shape[1] > idx:
            val = int(d[1, idx])
            id = d[0, idx]
            if id == '.':
                pos += val
                idx += 1
                continue
            id = int(id)
            for j in range(1, val + 1):
                print(id, '*' , pos)
                result += pos * id
                pos += 1
            idx += 1
        
        return result


if __name__ == "__main__":
    solution = Day9()
    solution.solve()
