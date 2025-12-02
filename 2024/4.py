from base import AoCBase
from typing import List
from re import findall, search
import numpy as np


class Day4(AoCBase):
    def __init__(self):
        super().__init__(4)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0

        data = np.array([list(row) for row in self.data])
        count = 0
        for i in range(0, 2):
            rot = np.rot90(data, i)
            print(rot)
            r = self.count(rot)
            print(i, r)
            count += r
            for ii in range(-len(rot) + 1, len(rot)):
                diag = np.diagonal(rot, ii)
                print(diag)
                rr = self.count(diag)
                print(ii, rr)
                count += rr

        result = count
        return result

    def count(self, data):
        flat = data.flatten()
        s = "".join(flat)
        return s.count("XMAS") + s.count("SAMX")

    def part2(self) -> int:
        data = np.array([list(row) for row in self.data])
        dict = {}
        count = 0
        print(data)
        re = r"(MAS|SAM)"
        for ii in range(-len(data) + 1, len(data)):
            diag = np.diagonal(data, ii)
            flat = diag.flatten()
            s = "".join(flat)
            matches = search(re, s)
            if matches is not None:
                idx = matches.start()
                dict[idx] = ii
                pass
        

        for k in dict:
            k



        return 0


if __name__ == "__main__":
    solution = Day4()
    solution.solve()
