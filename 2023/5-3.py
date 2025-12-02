import re
import time

def main():
    with open("/Users/samuelenocsson/dev/advent-of-code/5-input.txt", 'r') as file:
        row_cache = {}
        start_time = time.time()
        seed_string = file.readline()
        lines = file.readlines()
        maps =[]
        for idx, line in enumerate(lines):
            numbers = [int(digit) for digit in re.findall(r'\d+', line)]
            if len(numbers) > 0:
                maps.append(numbers)
        
        seeds = [int(digit) for digit in re.findall(r'\d+', seed_string)]
        for seed in seeds:
            sources = []
            sources.append(seed)
            for m in maps:
                current = sources.pop()
                current_start = current[0]
                current_end = current[1]
                


        location = -1
        next = 0

if __name__ == "__main__":
    main()