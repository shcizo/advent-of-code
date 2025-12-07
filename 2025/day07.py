"""Day X: Advent of Code 2025."""

import time
from collections import defaultdict
from aoc import read_lines, read_input, read_grid, read_ints
import numpy as np
from functools import lru_cache



def traverse(start_pos: tuple[int, int], data: np.ndarray, visited: set, collisions: set):
    start_row, start_col = start_pos
    if (start_row, start_col) in visited:
        return
    
    visited.add((start_row, start_col))
    row, col = data.shape
    r = start_row +  1
    while True:
        if r >= row:
            break
        v = data[r, start_col]
        if (r, start_col) in collisions:
            break
        if  v == '^':
            collisions.add((r, start_col))
            if start_col + 1 < col:
                traverse((r, start_col + 1), data, visited, collisions)
            if start_col - 1 >= 0:
                traverse((r, start_col - 1), data, visited, collisions)
            break
        
        r += 1
            
    return

def traverse_2(start_pos: tuple[int, int], data: np.ndarray, cache=None):
    if cache is None:
        cache = {}
    if start_pos in cache:
        return cache[start_pos]

    start_row, start_col = start_pos
    row, col = data.shape
    r = start_row + 1
    counter = 0

    while True:
        if r >= row:
            cache[start_pos] = counter + 1
            return counter + 1
        v = data[r, start_col]

        if v == '^':
            if start_col + 1 < col:
                counter += traverse_2((r, start_col + 1), data, cache)
            if start_col - 1 >= 0:
                counter += traverse_2((r, start_col - 1), data, cache)
            break

        r += 1

    cache[start_pos] = counter
    return counter
        
def part1(data: np.ndarray):
    rows, cols = np.where(data == 'S')
    if len(rows) == 0:
        raise ValueError("Start 'S' not found in grid")
    start_row, start_col = int(rows[0]), int(cols[0])
    collision = set()
    visited = set()
    traverse((start_row, start_col), data, visited, collision)
    print(data)
    return len(collision)


def part2(data):
    rows, cols = np.where(data == 'S')
    if len(rows) == 0:
        raise ValueError("Start 'S' not found in grid")
    start_row, start_col = int(rows[0]), int(cols[0])
    counter = traverse_2((start_row, start_col), data)
    return counter


if __name__ == "__main__":
    DAY = 7  # <- ändra till rätt dag
    data = read_grid(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
