import re

class T:
    def __init__(self, id, winning, card):
        self.id = id
        self.winning = winning
        self.card = card
        self.instances = 1
        self.intersect = len((list)(set(winning) & set(card)))

    def addInstance(self):
        self.instances += 1
        

def main():
    with open("4-input.txt", 'r') as file:
        array = []
        for line in file:
            array.append(parseLine(line))
        for i, card in enumerate(array):
            for ii in range(0, card.instances):
                for iii in range(i+1, i + 1 + card.intersect):
                    array[iii].addInstance()
        instancesArr = list(map(lambda x: x.instances, array))
        
        print(sum(instancesArr))

def parseLine(s: str):
    idSplit = s.split(":")
    id = getID(idSplit[0])

    cardSplit = idSplit[1].split("|")
    winning = re.findall(r'\d+', cardSplit[0])
    card = re.findall(r'\d+', cardSplit[1])
    cardInstance = T(id, winning, card)
    return cardInstance

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