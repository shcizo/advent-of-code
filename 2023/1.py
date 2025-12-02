import re;

numbers = [
    "zero",
    "one", 
    "two", 
    "three",
    "four",
    "five",
    "six",     
    "seven",
    "eight",
    "nine"
]

def main():
    totalvalue = 0
    with open("1-input.txt", 'r') as file:
       
        for line in file:
            line = line.strip()
            word = ''
            digits = []
            for s in line:
                nr = get_number(s)
                if nr == None:
                    word += s
                    nr = get_number(word)
                if nr != None: 
                    digits.append(nr)
                    break
            word = ''
            for i in range(len(line) - 1, -1, -1):
                s = line[i]
                nr = get_number(s)
                if nr == None:
                    word = s + word
                    nr = get_number(word)
                if nr != None: 
                    digits.append(nr)
                    break
            if len(digits) == 2: totalvalue += digits[0] * 10 + digits[1]
    print(totalvalue)

def get_number(s):
    if s.isnumeric(): 
        return int(s)
    for n in numbers:
        if s.count(n) > 0:
            return numbers.index(n)
    return None
        
def isDigit(s: str, a: list):
    digits = re.findall("\d", s)
    if (digits.__len__() > 0):
        return a.append
    for n in numbers:
        if (s.contains(n["s"])):
            return n["n"]
    return a;
    
if __name__ == "__main__":
    main()
