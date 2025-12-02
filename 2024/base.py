# base.py
from pathlib import Path
from typing import Any
from abc import ABC, abstractmethod

class AoCBase(ABC):
    def __init__(self, day: int):
        self.day = day
        self.raw_data = self.read_input()
        self.data = self.parse_input()

    def read_input(self) -> str:
        """Read input file."""
        return Path(f"inputs/day{self.day}.txt").read_text()

    @abstractmethod
    def parse_input(self) -> Any:
        """Parse the input data as needed."""
        pass

    @abstractmethod
    def part1(self) -> Any:
        """Solve part 1."""
        pass

    @abstractmethod
    def part2(self) -> Any:
        """Solve part 2."""
        pass

    def solve(self):
        """Solve both parts and print results."""
        print(f"Day {self.day}")
        print(f"Part 1: {self.part1()}")
        print(f"Part 2: {self.part2()}")