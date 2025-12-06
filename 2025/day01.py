"""Day 1: Advent of Code 2025."""

import time
from aoc import read_lines, read_input
    
def get_pointer(dial, move, pointer):
    dir = move[0]
    n = int(move[1:])
    if dir == 'L':
        pointer = (pointer - n) % len(dial)
    elif dir == 'R':
        pointer = (pointer + n) % len(dial)
    return dial[pointer]

def part1(data):
    dial = range(100)
    password = 0
    pointer = 50
    for line in data:
        move = line.strip()
        pointer = get_pointer(dial, move, pointer)
        if pointer == 0:
            password += 1

    return password

def get_new_index(dial, move, pointer):
    dir = move[0]
    n = int(move[1:])
    if dir == 'L':
        pointer = (pointer - n)
    elif dir == 'R':
        pointer = (pointer + n)
    return pointer

def part2(data):
    dial = range(100)
    password = 0
    pointer = 50
    for line in data:
        move = line.strip()
        if len(move[1:]) > 2:
            n = int(move[1:][:-2])
            move = move[0] + move[-2:]
            password += n
        
        idx = get_new_index(dial, move, pointer)
        if pointer != 0 and (idx < 0 or idx > len(dial)):
            password += 1
        pointer = idx % len(dial)
        if pointer == 0:
            password += 1
        

    return password



if __name__ == "__main__":
    data = read_lines(1)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
