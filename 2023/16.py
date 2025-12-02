import numpy as np


class Beam:
    def __init__(self, start_loc: tuple, current_loc: tuple):
        self.start_loc = start_loc
        self.current_loc = current_loc
        self.direction = None
        self.beam_length = 0
        self.energized = set()
        self.active = True

    def move(self, matrix: np.ndarray):
        if self.direction is None:
            self.direction = matrix[self.current_loc]
        next_loc = get_next(self.current_loc, self.direction, matrix.shape)
        if not (0 <= next_loc[0] < matrix.shape[0] and 0 <= next_loc[1] < matrix.shape[1]):
            self.active = False
            return None
        self.current_loc = next_loc
        self.beam_length += 1
        return next_loc
    
def get_next(prev_loc: tuple, direction: str, shape: tuple):
    match direction:
        case '-':
            return (prev_loc[0], prev_loc[1] - 1)
        case '/':
            return (prev_loc[0], prev_loc[1] + 1)
        case '\\':
            return (prev_loc[0] - 1, prev_loc[1])
        case '|':
            return (prev_loc[0] + 1, prev_loc[1])
        case '.':
            return prev_loc

file_path = '16-input.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
# Split each line into individual characters
lines = [list(line.strip()) for line in lines]

# Build a NumPy matrix of all the lines
matrix = np.array(lines)
shape = matrix.shape
traverse = True
current_loc = (0, 0)
beams = []
beams.append(Beam(current_loc, current_loc))
while(traverse):
    for beam in beams:
        if beam.active:
            next = beam.move(matrix)




