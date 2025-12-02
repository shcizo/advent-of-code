import re
import math

def main():
    with open("8-input.txt", 'r') as file:
        maps = {}
        starting_nodes = []
        lines = file.readlines()
        directions = re.findall("[a-zA-Z]", lines[0])

        for i, line in enumerate(lines[2:]):
            parsed = re.findall("[a-zA-Z]+", line)
            if len(parsed) == 0: continue
            if parsed[0].endswith('A'): starting_nodes.append(parsed[0])
            maps[parsed[0]] = (parsed[1], parsed[2])
        
        steps = []
        for starter in starting_nodes:
            steps.append(traverse_map(maps, directions, maps[starter], 0))
        print(steps)
        print(find_lcm_of_array(steps))

def find_lcm_of_array(arr):
    # Ensure the array is not empty
    if not arr:
        return None
    
    # Initialize lcm with the first element of the array
    lcm_result = arr[0]

    # Iterate through the array and find the LCM
    for i in range(1, len(arr)):
        lcm_result = math.lcm(lcm_result, arr[i])

    return lcm_result


def traverse_map(maps, directions, nd, steps):
    while(True):
        step = steps % len(directions)
        dir = directions[step]
        if dir == "R":
            next = nd[1]
        if dir == "L":
            next = nd[0]
        steps += 1
        if next.endswith('Z'): 
            return steps
        nd = maps[next]

if __name__ == "__main__":
    main()
