from base import AoCBase
from typing import List
from re import findall


class Day2(AoCBase):
    def __init__(self):
        super().__init__(2)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0
        regex = r"(\d+)"
        safe_increment = 3
        for line in self.data:
            valid = True
            matches = findall(regex, line)
            numbers = list((int(match) for match in matches))

            previous = None
            current = None
            is_increase = numbers[0] < numbers[len(numbers) - 1]

            for number in numbers:
                previous = current
                current = number
                if previous is None or current is None:
                    continue
                if (
                    abs(previous - current) > safe_increment
                    or previous == current
                    or is_increase != (previous < current)
                ):
                    valid = False
                    break

            if valid:
                result += 1
        return result

    def part2(self) -> int:
        result = 0
        regex = r"(\d+)"
        safe_increment = 3
        for line in self.data:
            valid = True
            matches = findall(regex, line)
            numbers = list((int(match) for match in matches))
            is_increase = numbers[0] < numbers[1]

            valid = self.is_safe(safe_increment, numbers, is_increase)

            if not valid:
                for i in range(0, len(numbers)):
                    n_copy = numbers.copy()
                    n_copy.pop(i)
                    is_increase = n_copy[0] < n_copy[1]
                    valid = self.is_safe(safe_increment, n_copy, is_increase)
                    if valid:
                        break

            if valid:
                result += 1
            else:
                print(f"Invalid numbers: {numbers}")
        return result

    def is_safe(self, safe_increment, numbers, is_increase):
        previous = None
        current = None
        valid = True
        for i in range(0, len(numbers)):
            previous = current
            current = numbers[i]
            if previous is None or current is None:
                continue
            if (
                abs(previous - current) > safe_increment
                or previous == current
                or is_increase != (previous < current)
            ):
                valid = False
                break
        return valid


if __name__ == "__main__":
    solution = Day2()
    solution.solve()
