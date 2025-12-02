import re

def main():
    with open("9-input.txt", 'r') as file:
        lines = file.readlines()
        values = []
        for line in lines:
            values.append(get_value(line))
        summerize = 0
        for v in values:
            summerize += v
        print(summerize)

def get_value(line: []):
    values = [int(digit) for digit in re.findall(r'-?\d+', line)]
    values.reverse()
    history = []
    history.append(values)
    for i, arr in enumerate(history):
        if all(value == 0 for value in arr): 
            break
        m = []
        history.append(m)
        for ii, val in enumerate(arr):
            if ii + 1 < len(arr):
                diff = arr[ii+1] - val
                m.append(diff)
    
    history.reverse()
    for i, arr in enumerate(history):
        if i == 0: 
            arr.append(0)
        else:
            last_value = arr[len(arr) - 1]
            next_value = last_value + history[i-1][len(history[i-1]) - 1]
            arr.append(next_value)
    last_index = len(history) - 1
    input_value = history[last_index][len(history[last_index]) - 2]
    last_value = history[last_index][len(history[last_index]) - 1]
    print(f"{input_value} -> {last_value}")
    return last_value

if __name__ == "__main__":
    main()