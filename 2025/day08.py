"""Day 8: Advent of Code 2025."""

import time
from aoc import read_lines
import math
from functools import reduce

def distance(start: tuple[int,int,int], end: tuple[int,int,int]):
    return math.sqrt(math.pow(start[0] - end[0], 2) + math.pow(start[1] - end[1], 2) + math.pow(start[2] - end[2], 2))
    

def part1(data):
    paths = {}
    i = 0
    while i < len(data):
        t = data[i]
        min_dist, closest = min((distance(t, y), y) for y in data if y != t)
        paths[tuple(t), tuple(closest)] = min_dist
        i += 1

    sp = list(sorted(paths.items(), key=lambda x: x[1]))
    circuits = []
    for jb in sp[10:]:
        t1, t2 = jb[0]
        matching = [i for i, c in enumerate(circuits) if t1 in c or t2 in c]
        if not matching:
            circuits.append({t1, t2})
        elif len(matching) == 1:
            circuits[matching[0]].update({t1, t2})
        else:
            # Merga circuits
            merged = {t1, t2}
            for i in sorted(matching, reverse=True):
                merged.update(circuits.pop(i))
            circuits.append(merged)
            
    

    
    pass


def part2(data):
    """Solve part 2."""
    pass


if __name__ == "__main__":
    DAY = 8  # <- ändra till rätt dag
    data = read_lines(DAY)
    array = [[int(x) for x in line.split(',')] for line in data]
    
    
    t0 = time.perf_counter()
    p1 = part1(array)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
