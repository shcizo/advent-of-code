
import os
import sys

import numpy as np

sys.path.insert(1, os.path.join(sys.path[0], ".."))
file_path = '14-test-input.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

map_ = {"#": -1, "O": 0, ".": 1}
array = np.array([[map_[char] for char in line.strip() ]for line in lines])
nrows, ncols = array.shape

def cycle(array):
    for i in range(4):
        array = roll(array)
        array = np.rot90(array, -1)
    return array


def hash_(array):
    return tuple(array.ravel())

def score(array):
    rolls = np.where(array == 0)[0]
    return (nrows - rolls).sum()


def roll(array):
    for i in range(ncols):
        rocks = [-1] + list(np.where(array[:, i] == -1)[0]) + [None]
        for j in range(len(rocks) - 1):
            left, right = rocks[j] + 1, rocks[j + 1]
            array[left:right, i] = np.sort(array[left:right, i])
    return array



seen = {}
scores = {}
maxval = 1_000_000_000
reverse_map = {-1: "#", 0: "O", 1: "."}
for i in range(maxval):
    h = hash_(array)
    if h in seen:
        print(array)
        print(f"Found cycle at {i+1}")
        break
    seen[h] = i
    scores[i] = score(array)
    array = cycle(array)
cycle_length = i - seen[h]
index = seen[h] + (maxval - seen[h]) % cycle_length
print(scores[index])