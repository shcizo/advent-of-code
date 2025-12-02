class Box:
    def __init__(self):
        self.lenses = []   

    def add_lens(self, lens_to_add):
        for i, lens in enumerate(self.lenses):
            if lens[0] == lens_to_add[0]:
                self.lenses[i] = lens_to_add
                return
        self.lenses.append(lens_to_add)
    
    def remove_lens(self, lens_to_remove):
        for i, lens in enumerate(self.lenses):
            if lens[0] == lens_to_remove[0]:
                self.lenses.pop(i)
                return

    def power(self, idx: int):
        total = 0
        if len(self.lenses) == 0:
            return 0
        for i, lens in enumerate(self.lenses):
            if lens[1] is None:
                continue
            total += lens[1] * (i + 1) * (idx + 1)
        
        return total        
    def __str__(self):
        return str(self.lenses)

def get_hash(word: str):
    array_total = 0
    ascii_num = [ord(char) for char in word]
    for num in ascii_num:
        array_total += num
        array_total *= 17
        array_total = array_total % 256
    return array_total


# Read the file
file_path = '15-input.txt'
with open(file_path, 'r') as file:
    line = file.readline()

# Split each line into individual characters
words = line.split(',')

boxes = [Box() for _ in range(256)]

print(words)
total = 0

for word in words:
    if word.count('-') == 1:
        start, end = word.split('-')
        box_idx = get_hash(start)
        boxes[box_idx].remove_lens((start, None))
    else:
        start, end = word.split('=')
        box_idx = get_hash(start)
        boxes[box_idx].add_lens((start, int(end)))

for i, box in enumerate(boxes):
    total += box.power(i)

print(total)