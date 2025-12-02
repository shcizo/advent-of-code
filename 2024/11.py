import math
import numpy as np
from base import AoCBase
from typing import List, Dict, Tuple
from re import findall
import cProfile

division_cache: Dict[int, Tuple[int, int]] = {}
digits_cache: Dict[int, int] = {}

class Day11(AoCBase):
    def __init__(self):
        super().__init__(11)  # Pass the day number to base class

    def parse_input(self) -> List[str]:
        """Override with specific parsing for this day."""
        return self.raw_data.strip()

    def part1(self) -> int:
        regex = r"(\d+)"
        numbers = findall(regex, self.data)
        data = np.array(numbers).astype(int)
        data = self.blink(data, 25)

        return len(data)

    def part2(self) -> int:
        regex = r"(\d+)"
        numbers = findall(regex, self.data)
        data = np.array(numbers).astype(int)
        data = self.blink(data, 40)

        return len(data)

    def blink(self, data, blinks):
        for i in range(blinks):
            arr = np.array(data)

            # Handle zero separately as it has special behavior
            arr[arr == 0] = 1

            # Calculate number of digits for all elements
            digit_counts = np.vectorize(lambda x: math.floor(math.log10(abs(x))) + 1 if x != 0 else 1)(arr)

            # Find indices of numbers with an even number of digits
            even_digit_indices = np.where(digit_counts % 2 == 0)

            # Iterate over these indices, split the numbers, and replace them
            new_data = []
            for idx in even_digit_indices[0]:
                n = arr[idx]
                num_digits = digit_counts[idx]
                first_half, second_half = split_number_in_half(n, num_digits)
                new_data.append(first_half)
                new_data.append(second_half)

            # Handle the rest of the numbers that do not meet the splitting condition
            for idx in range(len(arr)):
                if idx not in even_digit_indices[0]:
                    new_data.append(arr[idx] * 2024 if arr[idx] != 0 else 1)

            data = new_data

        return data

def count_digits(arr):
    return np.vectorize(lambda x: math.floor(math.log10(abs(x))) + 1 if x != 0 else 1)(arr)

precomputed_divisors = {i: 10**i for i in range(1, 20)}  # Adjust the range as needed

def split_number_in_half(number, num_digits):
    key = (number, num_digits)
    if key in division_cache:
        return division_cache[key]

    half = num_digits // 2
    divisor = precomputed_divisors.get(half, 10**half)

    first_half = number // divisor
    second_half = number % divisor
    division_cache[key] = (first_half, second_half)

    return first_half, second_half


if __name__ == "__main__":
    solution = Day11()
    #solution.solve()
    cProfile.run("solution.solve()")
