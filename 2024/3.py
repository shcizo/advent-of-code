from base import AoCBase
from typing import List
from re import findall


class Day3(AoCBase):
    def __init__(self):
        super().__init__(3)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip()

    def part1(self) -> int:
        result = 0
        regex = r"mul\((\d{1,3},\d{1,3})\)"
        data = self.raw_data.split("/n")
        for line in data:
            matches = findall(regex, line)
            for match in matches:
                n = match.split(",")
                result += int(n[0]) * int(n[1])
                pass
                
            
        return result

    def part2(self) -> int:
        result = 0
        regex = r"(mul\((\d{1,3},\d{1,3})\))|(do(?!n't))|(don't)"
        skip = False
        matches = findall(regex, self.data)
        for match in matches:
            if match[2] != "":
                skip = False
            elif match[3] != "":
                skip = True
            if match[1] != "" and skip is False:
                n = match[1].split(",")
                result += int(n[0]) * int(n[1])

                
        return result


if __name__ == "__main__":
    solution = Day3()
    solution.solve()
