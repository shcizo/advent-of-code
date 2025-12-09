"""Day X: Advent of Code 2025."""

import time
from itertools import combinations
from aoc import read_lines
from shapely.geometry import Polygon, box
from shapely.prepared import prep


def calculate_area(corner1, corner2):
    """Räknar ut arean av en rektangel givet två motstående hörn."""
    x1, y1 = map(int, corner1.split(","))
    x2, y2 = map(int, corner2.split(","))
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height

def create_box(corner1, corner2):
    """Räknar ut arean av en rektangel givet två motstående hörn."""
    x1, y1 = map(int, corner1.split(","))
    x2, y2 = map(int, corner2.split(","))
    return box(x1,y1,x2,y2)

def parse_coord(s):
      x, y = s.split(",")
      return (int(x), int(y))

def part1(data):
    max_size = 0
    for c1, c2 in combinations(data, 2):
        area = calculate_area(c1, c2)
        if area > max_size:
            max_size = area
    return max_size


def part2(data):
    coords = [parse_coord(line) for line in data]
    shape = Polygon(coords)
    prepared_shape = prep(shape)
    max_size = 0
    for c1, c2 in combinations(data, 2):
        area = calculate_area(c1, c2)
        if area > max_size:
            box = create_box(c1, c2)
            if prepared_shape.contains(box):
                max_size = area
    return max_size


if __name__ == "__main__":
    DAY = 9  # <- ändra till rätt dag
    data = read_lines(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
