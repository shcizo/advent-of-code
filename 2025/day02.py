from aoc import read_lines, read_input
from aoc.helpers import read_lines_and_split

def part1(data):
    ids = []
    for line in data:
        n = line.strip().split("-")
        r = range(int(n[0]), int(n[1]) + 1)
        for rr in r:
            ss = str(rr)
            if (len(ss) % 2) == 0:
                f = ss[:len(ss)//2]
                s = ss[len(ss)//2:]
                if f == s:
                    ids.append(rr)
    
    return sum(ids)

def find_pattern(s):
    if len(s) < 2:
        return False
    n = int(s)
    if all_same(n):
        print(f"Found pattern: {n}")
        return True
    for i in range(2, len(s) // 2 + 1):
        pattern = s[:i]
        repeated = pattern * (len(s) // i)
        if str(repeated) == s:
            print(f"Found pattern: {pattern} in {s}")
            return True 
    return False
        
def all_same(n):
    return len(set(str(n))) == 1         

def part2(data):
    ids = []    
    for line in data:
        n = line.strip().split("-")
        r = range(int(n[0]), int(n[1]) + 1)
        for rr in r:
            ss = str(rr)
            if find_pattern(ss):
                ids.append(rr)

    return sum(ids)

if __name__ == "__main__":
    data = read_lines_and_split(2, ",")  # or read_input(2), read_ints(2), read_grid(2)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")