"""Day X: Advent of Code 2025."""

import time
from aoc import split_grid_on_cols, read_input, read_grid, read_ints
import numpy as np
import operator
from functools import reduce

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow,
}

def part1(data: np.ndarray):
    totals = []
    rows, cols = data.shape
    for i in range(0, cols):
        numbers = []
        operator = data[rows - 1][i]
        for ii in range(0, rows - 1):
            numbers.append(int(data[ii][i]))
        op = ops[operator]
        totals.append(reduce(op, numbers))
    
    return sum(totals)


def part2(data: np.ndarray):
    totals = []
    grids = split_grid_on_cols(data)

    for i in range(0, len(grids)):
        numbers = []
        grid = np.array(grids[i])
        r, _ = grid.shape
        operator = str(grid[-1:][0][0])
        flipped = np.rot90(grid[:-1])
        nr, _ = flipped.shape
        for ii in range(0, nr):
            numbers.append(int(reduce(lambda a,b: a + b, flipped[ii])))
        op = ops[operator]
        r_total = reduce(op, numbers)
        print(f"{numbers}, op: {op}: total: {r_total}")
        totals.append(r_total)
    
    return sum(totals)


if __name__ == "__main__":
    DAY = 6  # <- ändra till rätt dag
    data = read_grid(DAY, str,  True)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    data = read_grid(DAY, str, keep_spaces=True)
    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
