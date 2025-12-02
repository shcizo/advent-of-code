import re

class Max:
    def __init__(self, id, red, blue, green):
        self.id = id
        self.red = red
        self.blue = blue
        self.green = green

    def isValid(self, maxRed, maxBlue, maxGreen):
        valid = self.red <= maxRed and self.blue <= maxBlue and self.green <= maxGreen
        return valid
    
    def power(self):
        return self.red * self.blue * self.green
        

def main():
    maxRed = 12
    maxBlue = 14
    maxGreen = 13
    with open("2-input.txt", 'r') as file:
        array = []
        for line in file:
            array.append(parseLine(line))
        result = 0
        power = 0
        for a in array:
            if(a.isValid(maxRed, maxBlue, maxGreen)):
                result += a.id
            power += a.power()
        print("power: " + power)
        print("id addition: " + result)

def parseLine(s: str):
    idSplit = s.split(":")
    id = getID(idSplit[0])
    green = 0
    blue = 0
    red = 0
    roundSplit = idSplit[1].split(";")
    for round in roundSplit:
        colorSplit = round.split(",")
        for color in colorSplit:
            green = max(green, getColor(color, "green"))
            blue = max(blue, getColor(color, "blue"))
            red = max(red, getColor(color, "red"))
    return Max(id, red, blue, green)


def getColor(s: str, color: str):
    split = s.strip().split(" ")
    if(color == split[1]):
        return int(split[0])
    return 0

def getID(split1):
    digs = re.findall("\d+", split1)
    id = digs[0]
    return int(id)

if __name__ == "__main__":
    main()