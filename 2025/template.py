"""Day X: Advent of Code 2025."""

import time
from aoc import read_lines, read_input, read_grid, read_ints


def part1(data):
    """Solve part 1."""
    pass


def part2(data):
    """Solve part 2."""
    pass


if __name__ == "__main__":
    DAY = 0  # <- ändra till rätt dag
    data = read_lines(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
