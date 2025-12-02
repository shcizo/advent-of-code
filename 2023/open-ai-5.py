import re
import time
from concurrent.futures import ProcessPoolExecutor

row_cache = {}

def main():
    with open("/Users/samuelenocsson/dev/advent-of-code/5-test-input.txt", 'r') as file:
        start_time = time.time()
        seed_string = file.readline()
        lines = file.readlines()
        lines_count = len(lines)
        digits = list(map(int, re.findall(r'\d+', seed_string)))
        next_index = 0
        for idx, line in enumerate(lines):
            numbers = [int(digit) for digit in re.findall(r'\d+', line)]
            row_cache[idx] = numbers

        with ProcessPoolExecutor() as executor:
            futures = []
            for i in range(0, len(digits), 2):
                first, first_range = digits[i], digits[i + 1]
                print(f"{first} -> {first + first_range}")
                end_range = first + first_range

                for s in range(first, end_range):
                    if s % 100000 == 0:
                        elapsed = time.time() - start_time
                        print(f"{s - first} done in {elapsed} seconds")

                    futures.append(executor.submit(get_location, lines_count, s))

                next_index += 2

            location = min(f.result() for f in futures)

        print(f"Closest location {location}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")

def get_location(nrLines, seed):
    init_seed = seed
    new_seed = seed
    fast_forward = False

    for i in range(0, nrLines):
        mappings = find_numbers(i)

        if len(mappings) > 0 and fast_forward:
            continue

        if len(mappings) == 0:
            fast_forward = False
            continue

        source, destination, _range = mappings

        if source <= seed <= source + _range:
            diff = seed - source
            new_seed = destination + diff
            fast_forward = True

    return new_seed

def find_numbers(idx):
    return row_cache[idx]

if __name__ == "__main__":
    main()
