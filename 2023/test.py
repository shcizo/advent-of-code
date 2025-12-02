def nextCharIsSymbol(line, index):
    for i, char in enumerate(line[index:], start=index):
        if not char.isdigit():
            return True
    return False

# Example usage:
my_line = "416.........................559...............417...............785.......900.......284...........503...796....992.........................."
my_index = 3

result = nextCharIsSymbol(my_line, my_index)
print(result)