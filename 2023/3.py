import re

def main():
    with open("3-input.txt", 'r') as file:
        lines = file.readlines()
        total = 0
        for line_index, line in enumerate(lines):
            print(f"Line: {line_index + 1}")
            digit = ""
            for index, char in enumerate(line):
                if char == '*' :
                    nr = []
                    print(f"found *")
                    for i in get_number(line, index-1, index +1):
                        print(f"found {i} on same row")
                        nr.append(i)
                    if(line_index - 1 >= 0):
                        for i in get_number(lines[line_index - 1], index-1, index +1):
                           print(f"found {i} on above row")
                           nr.append(i) 
                    if(line_index + 1 < len(lines)):
                        for i in get_number(lines[line_index + 1], index-1, index +1):
                           print(f"found {i} on lower row")
                           nr.append(i) 
                    if len(nr) == 2: 
                        total += int(nr[0]) * int(nr[1])

    print(total)

def get_number(line: str, from_index: int, to_index: int):
    res = find_digits_with_index(line)
    numbers = []
    for seq, idx in res:
        if ranges_intersect(range(idx, idx + len(seq) - 1), range(from_index, to_index)): numbers.append(seq)
    return numbers

def find_digits_with_index(input_string):
    pattern = re.compile(r'(\d+)')
    matches = pattern.finditer(input_string)

    result = [(match.group(), match.start()) for match in matches]
    return result

def ranges_intersect(range1:range, range2:range):
    # Check if either range's start is within the other range
    if range1.start <= range2.stop and range2.start <= range1.stop:
        return True
    else:
        return False

# titta i en line från index -> index
def has_symbol(line: [], from_index: int, to_index: int):
    if from_index < 0: from_index = 0
    for i, char in enumerate(line[from_index:]):
        if(i + from_index > to_index):
            return False
        if(not notDigit(char)):
            return False
        if(isSymbol(char)):
            return True
    return False        

def isPartNumber(line: [], first_index: int, last_index: int):
    is_match = False
    if(first_index > 0):
        is_match = isSymbol(line[first_index])
    return is_match or (last_index < len(line) and isSymbol(line[last_index]))

def isSymbol(s: str):
    pattern = r'[^0-9.\n]'
    return re.match(pattern, s)

def notDigit(s: str):
    match = re.findall("\d", s)
    return len(match) == 0

if __name__ == "__main__":
    main()