"""
Module to compute stats on small integer
"""
from collections import defaultdict
from validators import validate_number_in_range


class Stats:
    """
    class that handles stats from a numeric list
    """

    def __init__(self, data: list) -> None:
        self.data: dict = defaultdict(int)
        for k in data:
            self.data[k] += 1

    def less(self, number: int) -> int:
        """Return the amount of numbers less than number in the instance list"""
        validate_number_in_range(number, 0, 1000)

        counter: int = 0
        for k in range(1, number):
            counter += self.data[k]
        return counter

    def greater(self, number: int) -> int:
        """Return the amount of number greater than number in the instance list"""
        validate_number_in_range(number, 0, 1000)

        counter: int = 0
        for k in range(number + 1, 1000):
            counter += self.data[k]
        return counter

    def between(self, start: int, end: int) -> int:
        """Return the amount of number in greater or equal than start
        and less or equal than end in the instance list"""
        validate_number_in_range(start, 0, 1000)
        validate_number_in_range(end, 0, 1000)

        counter: int = 0
        for k in range(start, end + 1):
            counter += self.data[k]
        return counter


class DataCapture:
    """
    Class that capture values on a iterable for further processing
    """

    def __init__(self) -> None:
        self.data: list = []

    def add(self, number: int) -> None:
        """Add a number to the instance list"""
        validate_number_in_range(number, 1, 999)

        self.data.append(number)

    def build_stats(self) -> Stats:
        """Build a Stats object using the current values on the instance list"""
        return Stats(self.data)
