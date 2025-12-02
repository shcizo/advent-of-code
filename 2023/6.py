import re

def main():
    with open("6-input.txt", 'r') as file:
        winning_distances = []
        lines = file.readlines()
        time = ''.join(re.findall('\d+', lines[0]))
        distance = ''.join(re.findall('\d+', lines[1]))
        result = calcualte_distance(int(time), int(distance))
        winning_distances.append(len(result))
        winning_totals = 1
        for value in winning_distances:
            winning_totals *= value
        print(winning_totals)
 
def calcualte_distance(time: int, distance: int):
    reaches_longer = []
    for i in range(0, time):
        d = i * (time - i)
        if d > distance: 
            reaches_longer.append(d)
    return reaches_longer

if __name__ == "__main__":
    main()