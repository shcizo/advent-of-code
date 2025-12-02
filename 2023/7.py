from functools import cmp_to_key

value = ["J","1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

class Hand:
    def __init__(self, hand: str, bet: int, power: int, unsorted_power: int):
        self.hand = hand
        self.bet = bet
        self.power = power
        self.unsorted_power = unsorted_power

    def bet(self):
        return self.bet
    
def main():
    with open("7-input.txt", 'r') as file:
        hands = []
        for line in file.readlines():
            line = line.strip()
            split = line.split(' ')
            hands.append(Hand(split[0], int(split[1]), power(split[0]), unsorted_power(split[0])))
        p = list(sorted(hands, key=cmp_to_key(custom_comparator), reverse=True))
        mapped= list(map(lambda x: (x.hand, x.power, x.bet), p))
        print(mapped)
        result = 0
        for i, hand in enumerate(p):
            rank = (len(p)-i)
            product = hand.bet * rank
            result = result + product
        print(result)

def custom_comparator(element1: Hand, element2:Hand):
    # Replace this with your own logic to compare two elements
    # Here, we are comparing based on the length of the strings
    
    if element1.power < element2.power:
        return -1
    elif element1.power > element2.power:
        return 1
    else:
        for i in range(0,5):
            v1 = value.index(element1.hand[i])
            v2 = value.index(element2.hand[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
    return 0

def unsorted_power(hand: str):
    unsorted_hand_power = 0
    for i, char in enumerate(hand):
        unsorted_hand_power += value.index(char) * (1000 - (pow(i, 2)))
    return int(unsorted_hand_power)

def power(hand: str):
    power = []
    j_count = hand.count("J")
    if j_count == 5: return 500
    for char in hand:
        if char == 'J': continue
        count=hand.count(char)
        t = (count, char, value.index(char))
        if count > 0 and power.count(t) == 0:
            power.append(t)
    s = sorted(power, key=lambda x: (x[0],x[2]),reverse=True)
    highest = s[0]
    nd_highest = None
    if len(s) > 1:
        nd_highest = s[1]
    
    count = highest[0]
    if count == 5 or count + j_count == 5: 
        return 500 #+ value.index(first[1])
    if count == 4 or count + j_count == 4: 
        return 400 #+ value.index(first[1])
    if count == 3 or count + j_count == 3:
        j_count = 0
        if nd_highest != None:
            second = nd_highest[0]
            if second == 2 or second + j_count == 2:
                return 300# + value.index(first[1]) + value.index(second[1])
        return 200# + value.index(first[1])
    if count == 2 or count + j_count == 2:
        j_left = count - j_count 
        second = nd_highest[0]
        if second == 2:
            return 150# + value.index(first[1]) + value.index(second[1])
        return 100# + value.index(first[1])
    return 1

if __name__ == "__main__":
    main()

