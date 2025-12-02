# day1.py
from base import AoCBase
from typing import List
import re


class Day1(AoCBase):
    def __init__(self):
        super().__init__(1)  # Pass the day number to base class

    def parse_input(self) -> List[int]:
        reg = r"(\d+)\s+(\d+)"
        raw = self.raw_data.strip().split("\n")
        data = []
        for line in raw:
            match = re.search(reg, line)
            if match:
                one = int(match.group(1))
                two = int(match.group(2))
                data.append([one, two])
                pass

        return data

    def part1(self) -> int:
        result = 0
        row1 = []
        row2 = []
        for tuple in self.data:
            row1.append(int(tuple[0]))
            row2.append(int(tuple[1]))
            pass

        row_sorted1 = sorted(row1)
        row_sorted2 = sorted(row2)

        distance = 0
        for i in range(len(row_sorted1)):
            distance += abs(row_sorted1[i] - row_sorted2[i])
            pass

        result = distance
        return result

    def part2(self) -> int:
        result = 0
        row1 = []
        row2 = []
        for tuple in self.data:
            row1.append(int(tuple[0]))
            row2.append(int(tuple[1]))
            pass

        for i in range(len(row1)):
            n = row1[i]
            count = row2.count(n)
            result += n * count

        return result


if __name__ == "__main__":
    solution = Day1()
    solution.solve()
