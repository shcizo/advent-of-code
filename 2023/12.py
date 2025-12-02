import numpy as np
import itertools
from itertools import groupby
import timeit

filename = "12-input.txt"

def main():
    with open(filename, "r") as file:
        combinations = []
        for line in file:
            combinations.append(get_combinations(line))

        print(sum(combinations))

def get_combinations(line: str):
    start_time = timeit.default_timer()
    #print(f"Finding combinations for {line}")
    split = line.split(" ")
    springs = np.array(list(split[0]))

    config = np.array(split[1].strip().split(",")).astype(int)
    question_marks_indices = np.nonzero(springs == '?')[0]

    all_combinations = []
    combinations = itertools.product(['#', '.'], repeat=len(question_marks_indices))
    for combination in combinations:
        test_array = springs.copy()
        for i, index in enumerate(question_marks_indices):
            test_array[index] = combination[i]
        if validate_combination(test_array, config):
            all_combinations.append(test_array)

    end_time = timeit.default_timer()

    execution_time = end_time - start_time
    print(f"combinations for {line} done in {execution_time} seconds. {len(all_combinations)} combinations found.")
    return len(all_combinations)

def validate_combination(springs: [], config: []):
    hash_indices = np.nonzero(springs == '#')[0]
    if len(hash_indices) != config.sum():
        return False
    groups = [list(group) for key, group in groupby(springs) if key == '#']
    for i, group in enumerate(groups):
        if len(group) != config[i]:
            return False
    return True


if __name__ == "__main__":
    main()