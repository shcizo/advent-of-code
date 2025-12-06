import time
from aoc import read_lines, read_input
from aoc.helpers import read_lines_and_split
import numpy as np

def part1(data) -> int:
    totals = 0
    for line in data:
        line_max = 0
        arrray = np.array([int(d) for d in str(line)])
        for i in range(len(arrray)):
            if i == len(arrray) - 1:
                break
            current = int(arrray[i]) * 10
            max_val = int(np.max(arrray[i+1:]))
            if current + max_val > line_max:
                line_max = current + max_val
        totals += line_max
    
    return totals

def part2(data):
    totals = 0
    for line in data:
        array = np.array([int(d) for d in str(line)])
        values = []
        for i in range(11, -1, -1):
            if i == 0:
                slice = array
            else:
                slice = array[:-i]

            max_val = np.max(slice)
            max_index = np.where(slice == max_val)[0][0] + 1
            values.append(max_val)
            array = array[max_index:]
        
        line_total = sum(d * 10**i for i, d in enumerate(values[::-1]))
        totals += line_total

        
    return totals

if __name__ == "__main__":
    data = read_lines(3, int)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")