from concurrent.futures import ProcessPoolExecutor
import re
import time



def main():
    with open("/Users/samuelenocsson/dev/advent-of-code/5-input.txt", 'r') as file:
        row_cache = {}
        start_time = time.time()
        seed_string = file.readline()
        lines = file.readlines()
        for idx, line in enumerate(lines):
            numbers = [int(digit) for digit in re.findall(r'\d+', line)]
            row_cache[idx] = numbers
            
        digits = [int(digit) for digit in re.findall(r'\d+', seed_string)]
        seeds = []
        location = -1
        next = 0

        with ProcessPoolExecutor() as executor:
            for i, d in enumerate(digits):
                if i != next: continue
                first = digits[i]
                first_range = digits[i+1]
                print(f"{first} -> {first + first_range}")
                results = []
                get_location(first, first_range, row_cache)


                next += 2
        #seeds = getSeeds(seed_string)
        
        #for seed in seeds:
            #seed = get_location(lines, seed)
            #locations.append(seed)
    #location = min(f.result() for f in seeds)
    location = min(seeds)
    print(f"Closest location {location}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

def chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def process(list, row_cache):
    seeds = []
    for s in list:
        #seeds.append(executor.submit(get_location, s))
        seeds.append(get_location(s, row_cache))
    #return min(f.result() for f in seeds)
    return min(seeds)

def get_location(from_seed, to_seed, row_cache):
    nrLines = len(row_cache)
    init_seed = seed
    #print(f"finding location for {seed}")
    new_seed = seed
    fast_forward = False
    for i in range(0, nrLines): 
        mappings = row_cache.get(i)
        if len(mappings) > 0 and fast_forward: continue
        if len(mappings) == 0: 
            fast_forward = False
            continue
        source = mappings[1]
        destination = mappings[0]
        r = mappings[2]
        if source <= seed <= source + r:
            diff = seed - source
            new_seed = destination + diff    
            fast_forward = True

        #print(f"{seed} -> {new_seed}")
        seed = new_seed
    #print(f"Location {init_seed} -> {seed}")
    return seed
        
def getSeeds(s: str):
    digits = [int(digit) for digit in re.findall(r'\d+', s)]
    seeds = []
    next = 0
    for i, d in enumerate(digits):
        if i != next: continue
        first = digits[i]
        first_range = digits[i+1]
        for nr in range(first, first + first_range):
            seeds.append(nr)
        next += 2
    return seeds

if __name__ == "__main__":
    main()