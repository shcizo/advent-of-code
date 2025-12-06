"""Day X: Advent of Code 2025."""

import time
from aoc import read_lines, read_input, read_grid, read_ints
import numpy as np

from aoc.helpers import DIRS_8

def neighbors(grid, row, col, dirs=DIRS_8):
    """Yield (row, col, value) for valid neighbors."""
    rows, cols = grid.shape
    for dr, dc in dirs:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc, grid[nr, nc]


def part1(data: np.ndarray):
    sum = 0
    for row, col in np.ndindex(data.shape):
        if data[row, col] != '@':
            continue
        l = list(neighbors(data, row, col))
        ats = len(list(filter(lambda x: x[2] == '@', l)))
        if ats < 4:
           sum += 1
            

    return sum

def part2(data: np.ndarray):
    sum = 0
    past_array = np.array([['']*data.shape[1]]*data.shape[0])
    
    while not np.equal(data, past_array).all():
        past_array = data.copy()
        for row, col in np.ndindex(data.shape):
            if data[row, col] != '@':
                continue
            l = list(neighbors(data, row, col))
            ats = len(list(filter(lambda x: x[2] == '@', l)))
            if ats < 4:
                sum += 1
                data[row, col] = '-'
                print(data)

    return sum

if __name__ == "__main__":
    DAY = 4
    data = read_grid(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
