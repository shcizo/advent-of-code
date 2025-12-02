import numpy as np
from base import AoCBase
from typing import List
from re import findall
from itertools import chain


class Day7(AoCBase):
    def __init__(self):
        super().__init__(7)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        return self.raw_data.strip().split("\n")

    def calc(self, sum, numbers, target) -> List[int]:
        if len(numbers) == 0:
            return sum

        sum_1 = self.calc(sum + numbers[0], numbers[1:], target)
        sum_2 = self.calc(sum * numbers[0], numbers[1:], target)

        return [sum_1, sum_2]

    def calc_part2(self, sum, numbers, target) -> List[int]:
        if len(numbers) == 0:
            return sum

        sum_1 = self.calc_part2(sum + numbers[0], numbers[1:], target)
        sum_2 = self.calc_part2(sum * numbers[0], numbers[1:], target)
        sum_str = str(sum) + "" + str(numbers[0])
        sum_3 = self.calc_part2(int(sum_str), numbers[1:], target)

        return [sum_1, sum_2, sum_3]

    def part1(self) -> int:
        result = 0
        regex = r"(\d+)"
        for line in self.data:
            numbers = findall(regex, line)
            target = int(numbers[0])
            numbers = list(map(int, numbers[1:]))
            sum_1 = self.calc(0, numbers, target)
            arr = np.array(sum_1)
            print(arr.flatten())
            targets = np.argwhere(arr == target)
            if len(targets) > 0:
                result += target

        return result

    def part2(self) -> int:
        result = 0
        result = 0
        regex = r"(\d+)"
        for line in self.data:
            numbers = findall(regex, line)
            target = int(numbers[0])
            numbers = list(map(int, numbers[1:]))
            sum_1 = self.calc_part2(0, numbers, target)
            arr = np.array(sum_1)
            print(arr.flatten())
            targets = np.argwhere(arr == target)
            if len(targets) > 0:
                result += target
        return result


if __name__ == "__main__":
    solution = Day7()
    solution.solve()
