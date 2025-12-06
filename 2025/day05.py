"""Day X: Advent of Code 2025."""

import time
from aoc import read_lines, read_input, read_grid, read_ints


def part1(data):
    n_array = []
    for i in range(0, len(data) - 1):
        line = data[i].strip()
        if line == '':
            data = data[i+1:]
            break
        nrs = line.split('-')
        n1 = int(nrs[0])
        n2 = int(nrs[1])
        n_array.append((n1, n2))

        
    sum = 0
    for number in data:
        i = int(number.strip())
        for nn in n_array:
            l, h = nn
            if i >= l and i <= h:
                sum += 1
                break
                
    return sum


def part2(data):
    n_array = []
    for line in data:
        if line == '':
            break
        nrs = line.split('-')
        n1 = int(nrs[0])
        n2 = int(nrs[1])
        n_array.append((n1, n2))
    
    sd = sorted(n_array, key=lambda p: p[0])
    merged = [sd[0]]
    for start, end in sd[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # överlappar
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
        
            
    
    total = 0
    for k,v in merged:
        total += v - k + 1
        
    return total


if __name__ == "__main__":
    DAY = 5  # <- ändra till rätt dag
    data = read_lines(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
