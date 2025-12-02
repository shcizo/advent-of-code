from base import AoCBase
from typing import List
import numpy as np


class Day12(AoCBase):
    def __init__(self):
        super().__init__(12)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0
        data = np.array([list(row) for row in self.data])
        unique_values = np.unique(data)
        print(unique_values)

        for value in unique_values:
            indices = np.argwhere(data == value)
            edges = set()
            for i in range(0, len(indices)):
                if i == 0:
                    edges.add(indices[i])
                    continue
            
            
                


        return result

    def part2(self) -> int:
        result = 0
        for line in self.data:
            pass
        return result


if __name__ == "__main__":
    solution = Day12()
    solution.solve()
