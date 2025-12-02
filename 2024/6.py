from base import AoCBase
from typing import List
from re import findall
import numpy as np


class Day6(AoCBase):
    def __init__(self):
        super().__init__(6)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0
        data = np.array([list(row) for row in self.data])

        

        
        return result


    def part2(self) -> int:
        result = 0
        for line in self.data:
            pass
        return result


if __name__ == "__main__":
    solution = Day6()
    solution.solve()
