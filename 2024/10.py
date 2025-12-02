import numpy as np
from base import AoCBase
from typing import List


class Day10(AoCBase):
    def __init__(self):
        super().__init__(10)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip().split("\n")

    def part1(self) -> int:
        result = 0
        trail_map = np.array([list(row) for row in self.data]).astype(int)
        starting_points = np.argwhere(trail_map == 0)
        for i in range(0, len(starting_points)):
            visited = set()
            print(starting_points[i])
            trails = find_trail(trail_map, starting_points[i], visited)
            result += trails
            print("found", trails)

        return result

    def part2(self) -> int:
        result = 0
        trail_map = np.array([list(row) for row in self.data]).astype(int)
        starting_points = np.argwhere(trail_map == 0)
        for i in range(0, len(starting_points)):
            visited = None
            print(starting_points[i])
            trails = find_trail(trail_map, starting_points[i], visited)
            result += trails
            print("found", trails)

        return result


def find_trail(trail_map, point, visited) -> int:
    trails = 0
    if visited is not None and (point[0], point[1]) in visited:
        return 0
    if visited is not None:
        visited.add((point[0], point[1]))
    number = trail_map[point[0], point[1]]
    print(point[0], point[1])
    if number == 9:
        print("found")
        return 1
    next_number = number + 1
    shape = trail_map.shape
    from_row = point[0] - 1
    to_row = point[0] + 2
    from_col = point[1] - 1
    to_col = point[1] + 2

    subset = trail_map[
        max(0, from_row) : min(shape[0], to_row),
        max(0, from_col) : min(shape[1], to_col),
    ]
    # print(subset)
    next_point = np.argwhere(subset == next_number)

    if len(next_point) == 0:
        return 0
    for i in range(0, len(next_point)):
        row = next_point[i][0] + max(0, from_row) 
        col = next_point[i][1] + max(0, from_col)
        if col != point[1] and row != point[0]:
            continue
        trails += find_trail(trail_map, (row, col), visited)

    return trails


if __name__ == "__main__":
    solution = Day10()
    solution.solve()
